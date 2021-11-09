from django.db import models
from meds.models import PrnMed, ScheduledMed

class MarPrn(models.Model):
    med = models.ForeignKey(PrnMed, on_delete=models.CASCADE)
    mar_datetime = models.DateTimeField()
    indication = models.CharField(max_length=200)
    initial = models.CharField(max_length=20)

    class Meta:
        ordering = ['-mar_datetime']

    def __str__(self):
        return f'{self.med.name} by {self.initial}'

class MarScheduled(models.Model):
    given = models.BooleanField(default=False)
    med = models.ForeignKey(ScheduledMed, on_delete=models.CASCADE)
    mar_date = models.DateField()
    time = models.CharField(max_length=200)
    nurse = models.CharField(max_length=20)


    class Meta:
        verbose_name_plural = "Mar scheduled"
