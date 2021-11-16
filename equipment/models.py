from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date
from django import forms



# Create your models here.
class CPAP(models.Model):
    
    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField()
    initials = models.CharField(max_length=200)

    def __str__(self):
        return self.equipment


class Suction(models.Model):
    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField(validators=[])
    initials = models.CharField(max_length=200)

    def __str__(self):
        return self.equipment



class Other(models.Model):

    equipment = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    date = models.DateField(validators=[])
    initials = models.CharField(max_length=200)

    def __str__(self):
        return self.equipment
