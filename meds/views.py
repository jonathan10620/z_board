from django.shortcuts import render, redirect
from .forms import ScheduledMedForm
from django.contrib import messages

# Create your views here.
def addmed(request):

    if request.method == "POST":
        form = ScheduledMedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Medication added")

            return redirect("home")

    context = {"form": ScheduledMedForm()}
    return render(request, "meds/addmed.html", context)
