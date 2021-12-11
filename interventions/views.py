import calendar
import datetime
from pprint import pprint

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FeedingForm
from .models import FeedingEntries


# Create your views here.
def interventions(request):
    day_of_week = datetime.datetime.now().weekday()
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")

    form = FeedingForm(request.POST or None)

    if request.method == 'POST':
        print('what is happening?')
        print(form.errors)
        if form.is_valid():
            print('form is valid')
            object = form.save(commit=False)
            object.feeding_choice = request.POST.get('feeding')
            object.day = day_of_week
            object.save()
            messages.success(request, "Feeding added")

            return redirect('interventions')
            

    FEEDING_CHOICES = (
        (0, 'first'),
        (1, 'second'),
        (2, 'third'),
        (3, 'fourth'),
        (4, 'fifth'),
    )

    objects = FeedingEntries.objects.all().order_by('day')

    table = [
        {'day': 'Monday', 'feedings': [None, None, None, None, None]},
        {'day': 'Tuesday', 'feedings': [None, None, None, None, None]},
        {'day': 'Wednesday', 'feedings': [None, None, None, None, None]},
        {'day': 'Thursday', 'feedings': [None, None, None, None, None]},
        {'day': 'Friday', 'feedings': [None, None, None, None, None]},
        {'day': 'Saturday', 'feedings': [None, None, None, None, None]},
        {'day': 'Sunday', 'feedings': [None, None, None, None, None]}
        ]
    
    for obj in objects:
        table[obj.day]['feedings'][obj.feeding_choice] = {'time': obj.time_given, 'initial': obj.initials}



    context = {'form': form, 'feeding_choices': FEEDING_CHOICES, 'table': table[:day_of_week + 1], 'current_day': calendar.day_name[day_of_week]}


    return render(request, 'interventions/interventions.html', context)