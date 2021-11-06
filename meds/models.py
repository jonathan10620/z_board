from django.db import models

# Create your models here.
class ScheduledMed(models.Model):
    name = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    frequency = models.CharField(max_length=200)
    times = models.CharField(max_length=200)

    def times_as_list(self):
        return self.times.split(" ")

    def time_count(self):
        return len(self.times.split(" "))

    def __str__(self):
        return self.name


class MarScheduled(models.Model):
    given = models.BooleanField(default=False)
    med = models.ForeignKey(ScheduledMed, on_delete=models.CASCADE)
    date = models.DateField()
    nurse = models.CharField(max_length=20)

    def weekday(self):
        return self.date.weekday()


class PrnMed(models.Model):
    name = models.CharField(max_length=200)
    dose = models.CharField(max_length=200)
    indication = models.CharField(max_length=200)

    def __str__(self):
        return self.name
