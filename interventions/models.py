from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime


class FeedingEntries(models.Model):
    def no_future(value):
        combined = datetime.datetime.combine(datetime.date.today(),value)
        if combined > datetime.datetime.now():
            raise ValidationError("Date cannot be in the future!")
    
    initials = models.CharField(max_length=100)
    time_given = models.TimeField(validators=[no_future])
    feeding_choice = models.IntegerField()
    day = models.IntegerField()

    isoweek = models.IntegerField()


class BreathingEntry(models.Model):
    def no_future(value):
        combined = datetime.datetime.combine(datetime.date.today(),value)
        if combined > datetime.datetime.now():
            raise ValidationError("Date cannot be in the future!")

    initials = models.CharField(max_length=100)
    time_given = models.TimeField(validators=[no_future])
    breathing_choice = models.IntegerField()
    day = models.IntegerField()

    isoweek = models.IntegerField()