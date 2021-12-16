import json
from datetime import date, datetime, timedelta
from pprint import pprint

from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import ordinal
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.utils.timezone import make_aware

from .forms import SeizureForm
from .models import Seizure

today = date.today()
dates = [
    today + timedelta(days=x)
    for x in range(0 - today.weekday(), 7 - today.weekday())
]
ord_date = [ordinal(dates[0].strftime("%d")), ordinal(dates[-1].strftime("%d"))]



# Create your views here.
def seizure(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    form = SeizureForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Seizure Succesfully Logged")
            return redirect('seizure')

    js_labels = []
    today = date.today()
    past_days_of_week = []

    for n in range(7):
        tmp_day = today - timedelta(days=today.weekday() - n)
        past_days_of_week.append(tmp_day)
        js_labels.append([tmp_day.strftime("%a"), tmp_day.strftime("%-m/%-d")])

    past_week_freq_data = []

    for sz_date in past_days_of_week:
        sz_date = datetime.combine(sz_date, datetime.min.time())
        if sz_date <= datetime.now():
            past_week_freq_data.append(
                Seizure.objects.filter(date__date=make_aware(sz_date)).count()
            )
        else:
            past_week_freq_data.append(None)

    pprint(past_week_freq_data)
    seizure_data = Seizure.objects.all()[:50]
    paginator = Paginator(seizure_data, 7) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
            'form': form, 
            'data': seizure_data,
            'page_obj': page_obj,
            'labels': json.dumps(js_labels), 
            'week_freq': json.dumps(past_week_freq_data),
            "week_dates": dates,
            "ord_date": ord_date,
            }


    return render(request, 'seizure/seizure.html', context)