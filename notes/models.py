from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)

    class Meta:
        ordering = ['-date']

    