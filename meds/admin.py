from django.contrib import admin

from .models import PrnMed, ScheduledMed

# Register your models here.
admin.site.register(ScheduledMed)
admin.site.register(PrnMed)
