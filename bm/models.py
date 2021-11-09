from django.db import models

# Create your models here.
class BM(models.Model):
    bm_sizes = [
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large')
    ]
    date = models.DateTimeField()
    size = models.CharField(max_length=20, choices=bm_sizes)
    comment = models.CharField(max_length=200, null=True, blank=True)
    initial = models.CharField(max_length=20)

    class Meta:
        ordering = ['-date']

    