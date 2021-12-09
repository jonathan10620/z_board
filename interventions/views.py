from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FeedingEntries
from datetime import date
from bm.forms import BMForm
from .forms import FeedingForm

# Create your views here.
def interventions(request):
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")

    
    form = FeedingForm()

    FEEDING_CHOICES = (
        (0, 'first feeding'),
        (1, 'second feeding'),
        (2, 'third feeding'),
        (3, 'fourth feeding'),
        (4, 'fifth feeding'),
    )



    context = {'form': form, 'feeding_choices': FEEDING_CHOICES}


    return render(request, 'interventions/interventions.html', context)