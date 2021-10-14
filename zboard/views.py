from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from meds.models import ScheduledMed, PrnMed


# Create your views here.
def login_user(request):

    if request.method == "POST":
        if request.POST["password"] != "purple":
            messages.add_message(request, messages.INFO, "Password incorrect")
            return redirect("login")
        else:
            messages.add_message(request, messages.SUCCESS, "Logged in succesfully")
            request.session["logged_in"] = True
            return redirect("home")

    return render(request, "zboard/login.html")


def home(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")

    sched_meds = ScheduledMed.objects.all()
    prn_meds = PrnMed.objects.all()

    context = {
        "scheduled_meds": sched_meds,
        "prn_meds": prn_meds,
        "contacts": Contact.objects.all(),
    }

    return render(request, "zboard/home.html", context)
