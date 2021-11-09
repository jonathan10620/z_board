from django.contrib import admin
from .models import ScheduledMed, PrnMed

# Register your models here.
admin.site.register(ScheduledMed)
admin.site.register(PrnMed)
