from django.db import models

# Create your models here.
class intervention(models.Model):
    pass


class FeedingEntries(models.Model):
    initials = models.CharField(max_length=100)
    time_given = models.TimeField()
    int_day = models.IntegerField()