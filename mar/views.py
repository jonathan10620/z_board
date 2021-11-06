from django.shortcuts import render, redirect
from meds.models import ScheduledMed
from meds.models import MarScheduled
from django.contrib.humanize.templatetags.humanize import ordinal
import datetime
from django.contrib import messages


# Create your views here.
def scheduled(request):
    today = datetime.date.today()
    dates = [
        today + datetime.timedelta(days=x)
        for x in range(0 - today.weekday(), 7 - today.weekday())
    ]

    sched_meds = ScheduledMed.objects.all()

    if request.method == "POST":
        messages.success(request, "MAR updated")
        return redirect("mar:scheduled")

    mar_entries = MarScheduled.objects.filter(date__range=(dates[0], dates[-1]))
    mar_map = []

    for med in sched_meds:
        mar_map.append({"med": med.name, "times": med.times})

    print(mar_map)

    weekday_slice = ":" + str(today.weekday() + 1)

    ord_date = [ordinal(dates[0].strftime("%d")), ordinal(dates[-1].strftime("%d"))]
    context = {
        "meds": sched_meds,
        "today": today,
        "week_dates": dates,
        "mar_map": mar_map,
        "ord_date": ord_date,
        "weekday_slice": weekday_slice,
    }

    return render(request, "mar/scheduled_mar.html", context)


def prn(request):
    return render(request, "mar/prn_mar.html")


# mar_array = []
# for med in sched_meds:
#     med_week = []
#     for day in dates[: today.weekday() + 1]:
#         for entry in mar_entries:
#             if entry.med == med.name and entry.date == day:
#                 med_week.append(
#                     {"med": med.name, "nurse": entry.nurse, "times": med.times}
#                 )
#                 break
#         else:
#             med_week.append({"med": med.name, "nurse": "", "times": med.times})
#     mar_array.append(med_week)
