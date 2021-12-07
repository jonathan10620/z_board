from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FeedingEntries

# Create your views here.
def interventions(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")
    
    context = {}

    return render(request, 'interventions/interventions.html', context)