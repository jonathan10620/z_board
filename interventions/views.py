import calendar
import datetime
from pprint import pprint

from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FeedingForm, BreathingForm
from .models import FeedingEntries, BreathingEntry


# Create your views here.
def interventions(request):
    day_of_week = datetime.datetime.now().weekday()
    if not request.session.get("logged_in"):
        messages.add_message(request, messages.INFO, "Please log in first")
        return redirect("login")

    if request.method == 'POST':
        if 'feeding_form' in request.POST:
            feed_form = FeedingForm(request.POST)

            if feed_form.is_valid():
                print('FEEDING FORM ENTERED')
                object = feed_form.save(commit=False)
                object.feeding_choice = request.POST.get('feeding')
                object.day = day_of_week
                object.isoweek = datetime.datetime.now().isocalendar()[1]
                object.save()
                messages.success(request, "Feeding added")
                return redirect('interventions')
            else:
                messages.warning(request, "Time can not be in future")

        else:
            breath_form = BreathingForm(request.POST)
            if breath_form.is_valid():
                object = breath_form.save(commit=False)
                object.breathing_choice = request.POST.get('breathing')
                object.day = day_of_week
                object.isoweek = datetime.datetime.now().isocalendar()[1]
                object.save()
                messages.success(request, "Breath Treatment added")
                return redirect('interventions')
            else:
                messages.warning(request, "Time can not be in future")

    feed_form = FeedingForm()
    
    FEEDING_CHOICES = (
        (0, 'first'),
        (1, 'second'),
        (2, 'third'),
        (3, 'fourth'),
        (4, 'fifth'),
    )

    feed_objects = FeedingEntries.objects.all().order_by('day').filter(isoweek=datetime.datetime.now().isocalendar()[1])


    feed_table = [
        {'day': 'Monday', 'feedings': [None, None, None, None, None]},
        {'day': 'Tuesday', 'feedings': [None, None, None, None, None]},
        {'day': 'Wednesday', 'feedings': [None, None, None, None, None]},
        {'day': 'Thursday', 'feedings': [None, None, None, None, None]},
        {'day': 'Friday', 'feedings': [None, None, None, None, None]},
        {'day': 'Saturday', 'feedings': [None, None, None, None, None]},
        {'day': 'Sunday', 'feedings': [None, None, None, None, None]}
        ]
    
    for obj in feed_objects:
        feed_table[obj.day]['feedings'][obj.feeding_choice] = {'time': obj.time_given, 'initial': obj.initials}

    breath_objects = BreathingEntry.objects.all().order_by('day').filter(isoweek=datetime.datetime.now().isocalendar()[1])

    breath_table = [
        {'day': 'Monday', 'breathing': [None, None,]},
        {'day': 'Tuesday', 'breathing': [None, None, ]},
        {'day': 'Wednesday', 'breathing': [None, None, ]},
        {'day': 'Thursday', 'breathing': [None, None, ]},
        {'day': 'Friday', 'breathing': [None, None, ]},
        {'day': 'Saturday', 'breathing': [None, None, ]},
        {'day': 'Sunday', 'breathing': [None, None,]}
        ]
    
    breath_form = BreathingForm()
    
    for obj in breath_objects:
        breath_table[obj.day]['breathing'][obj.breathing_choice] = {'time': obj.time_given, 'initial': obj.initials}
        

    context = {
        'breath_form': breath_form,
        'form':feed_form, 
        'breath_form':breath_form,
        'feeding_choices': FEEDING_CHOICES, 
        'feed_table': feed_table[:day_of_week + 1],
        'breath_table': breath_table[:day_of_week + 1],
        'current_day': calendar.day_name[day_of_week]
        }


    return render(request, 'interventions/interventions.html', context)