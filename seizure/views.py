from django.shortcuts import render, redirect
from .forms import SeizureForm
from .models import Seizure
from django.contrib import messages
from datetime import timedelta
from django.utils.timezone import make_aware
from datetime import date
from datetime import datetime





# Create your views here.
def seizure(request):
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

            


    seizure_data = Seizure.objects.all()

    context = {'form': form, 'data': seizure_data}

    return render(request, 'seizure/seizure.html', context)