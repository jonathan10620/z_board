from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# Create your models here.
class BM(models.Model):
    def no_future(value):
        if value > timezone.now():
            raise ValidationError("Date cannot be in the future!")


    bm_sizes = [
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large')
    ]
    date = models.DateTimeField(validators=[no_future])
    size = models.CharField(max_length=20, choices=bm_sizes)
    comment = models.CharField(max_length=200, null=True, blank=True)
    initial = models.CharField(max_length=20)

    class Meta:
        ordering = ['-date']

    