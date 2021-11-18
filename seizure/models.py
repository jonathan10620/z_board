from django.db import models

# Create your models here.

class Seizure(models.Model):
    date = models.DateTimeField()
    duration = models.IntegerField()
    action = models.CharField(max_length=100)
    initial = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Seizures'
        ordering = ['-date']

    def __str__(self):
        return self.initial