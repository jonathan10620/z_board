from django.db import models

# Create your models here.
class CPAP(models.Model):
    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField()
    initials = models.CharField(max_length=200)


class Suction(models.Model):
    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField()
    initials = models.CharField(max_length=200)


class Other(models.Model):
    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField()
    initials = models.CharField(max_length=200)

