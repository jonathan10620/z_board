from django.db import models

# Create your models here.
class ScheduledMed(models.Model):
    name = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    times = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PrnMed(models.Model):
    name = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    indication = models.CharField(max_length=200)

    def __str__(self):
        return self.name
