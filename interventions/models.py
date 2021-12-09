from django.db import models


class FeedingEntries(models.Model):
    initials = models.CharField(max_length=100)
    time_given = models.TimeField()
    feeding_choice = models.IntegerField()
    day = models.IntegerField()