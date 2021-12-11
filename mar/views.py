import datetime
import pprint

from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import ordinal
from django.shortcuts import redirect, render

from meds.models import PrnMed, ScheduledMed

from .forms import PrnMarForm
from .models import MarPrn, MarScheduled

today = datetime.date.today()
dates = [
    today + datetime.timedelta(days=x)
    for x in range(0 - today.weekday(), 7 - today.weekday())
]
ord_date = [ordinal(dates[0].strftime("%d")), ordinal(dates[-1].strftime("%d"))]

# Create your views here.
def scheduled(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    sched_meds = ScheduledMed.objects.all()

    if request.method == "POST":
        nurse = request.POST.get("nurse")
        if not nurse:
            messages.info(request, "Enter Initials")
            return redirect("mar:scheduled")

        med = ScheduledMed.objects.filter(name=request.POST.get("med")).first()
        date = request.POST.get("date").replace('.', '').replace(',', '')
        time = request.POST.get("time")

        date_formatted = datetime.datetime.strptime(date, "%b %d %Y")

        mar_object = MarScheduled(given=True, med=med, mar_date=date_formatted, nurse=nurse, time=time)

        mar_object.save()

        messages.success(request, "MAR updated")
        return redirect("mar:scheduled")

    mar_entries = MarScheduled.objects.filter(mar_date__range=(dates[0], dates[-1]))
    mar_map = []

    for med in sched_meds:
        mar_map.append({"med": med, "times": med.times.split(' '), "days": []})
        for time in med.times.split(' '):
            for date in dates:
                for entry in mar_entries:
                    if entry.mar_date == date and entry.time == time and entry.med == med:
                        mar_map[-1]["days"].append({"date": date, "time": time, "nurse": entry.nurse})
                        break
                else:
                    mar_map[-1]["days"].append({"date": date, "time": time, "nurse": None})

    
    context = {
        "meds": sched_meds,
        "today": today,
        "week_dates": dates,
        "ord_date": ord_date,
        "mar_map": mar_map,
    }

    return render(request, "mar/scheduled_mar.html", context)


def prn(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    form = PrnMarForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "MAR updated")
            return redirect("mar:prn")


    prn_meds = PrnMed.objects.all()
    mars = MarPrn.objects.all()[:20]

    context = {
        'form': form,
        'prns': mars
    }

    return render(request, "mar/prn_mar.html", context)

