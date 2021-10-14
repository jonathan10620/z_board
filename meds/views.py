from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import ScheduledMedForm, PrnMedForm
from .models import ScheduledMed, PrnMed
from django.contrib import messages

from django.views.decorators.http import require_http_methods

# Create your views here.
def add_schedule(request):
    if request.method == "POST":
        form = ScheduledMedForm(request.POST)
        if form.is_valid():
            obj = ScheduledMed()
            obj.name = form.cleaned_data["name"]
            obj.dose = form.cleaned_data["dose"]
            obj.frequency = form.cleaned_data["frequency"]
            obj.times = form.cleaned_data["times"]
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Medication added")

            return redirect("home")

    context = {"form": ScheduledMedForm()}
    return render(request, "meds/add_sched.html", context)


def detail_schedule(request, id):
    med = ScheduledMed.objects.get(id=id)
    return render(request, "meds/detail_sched.html", {"med": med})


@require_http_methods(["POST"])
def delete_schedule(request, id):
    if request.method == "POST":
        med = ScheduledMed.objects.get(id=id)
        med.delete()
        messages.add_message(request, messages.INFO, "Medication deleted")
        return redirect("home")


# PRN Views
def add_prn(request):
    if request.method == "POST":
        form = PrnMedForm(request.POST)
        if form.is_valid():
            obj = PrnMed()
            obj.name = form.cleaned_data["name"]
            obj.dose = form.cleaned_data["dose"]
            obj.indication = form.cleaned_data["indication"]
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Medication added")

            return redirect("home")

    context = {"form": PrnMedForm()}
    return render(request, "meds/add_prn.html", context)


def detail_prn(request, id):
    med = PrnMed.objects.get(id=id)
    return render(request, "meds/detail_prn.html", {"med": med})


@require_http_methods(["POST"])
def delete_prn(request, id):
    if request.method == "POST":
        med = PrnMed.objects.get(id=id)
        med.delete()
        messages.add_message(request, messages.INFO, "Medication deleted")
        return redirect("home")
