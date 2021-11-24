from django.shortcuts import render, redirect
from .forms import SeizureForm
from .models import Seizure
from django.contrib import messages
from datetime import timedelta
from django.utils.timezone import make_aware
from datetime import date
from datetime import datetime
import json
from django.core.paginator import Paginator





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
            past_week_freq_data.append(0)


    seizure_data = Seizure.objects.all()[:50]
    paginator = Paginator(seizure_data, 7) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
            'form': form, 
            'data': seizure_data,
            'page_obj': page_obj,
            'labels': json.dumps(js_labels), 
            'week_freq': json.dumps(past_week_freq_data)
            }


    return render(request, 'seizure/seizure.html', context)