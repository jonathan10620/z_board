from django.db import models

# Create your models here.
class Mar(models.Model):
    
    date = models.DateField()
    time = models.CharField(max_length=200, null=True, blank=True)
    nurse = models.CharField(max_length=200)
    med = models.CharField(max_length=200)
    given = models.BooleanField(default=False)
