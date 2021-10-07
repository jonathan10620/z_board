from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact


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
    sched_meds = [
        {"name": "sample1", "dose": "100mg", "frequency": "BID", "times": "07:00"},
        {"name": "sample2", "dose": "250mg", "frequency": "TID", "times": "1300"},
        {"name": "sample3", "dose": "300mg", "frequency": "QD", "times": "0700"},
        {"name": "sample4", "dose": "1500mg", "frequency": "BID", "times": "0700 1300"},
        {"name": "sample5", "dose": "2.5mg", "frequency": "BID", "times": "1930"},
    ]
    prn_meds = [
        {"name": "sample1", "dose": "100mg", "frequency": "BID", "times": "07:00"},
        {"name": "sample2", "dose": "250mg", "frequency": "TID", "times": "1300"},
        {"name": "sample3", "dose": "300mg", "frequency": "QD", "times": "0700"},
        {"name": "sample4", "dose": "1500mg", "frequency": "BID", "times": "0700 1300"},
        {"name": "sample5", "dose": "2.5mg", "frequency": "BID", "times": "1930"},
    ]

    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in")
        return redirect("login")

    context = {
        "scheduled_meds": sched_meds,
        "prn_meds": prn_meds,
        "contacts": Contact.objects.all(),
    }

    return render(request, "zboard/home.html", context)
