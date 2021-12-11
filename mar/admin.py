from django.contrib import admin

from .models import MarPrn, MarScheduled

# Register your models here.
admin.site.register(MarScheduled)
admin.site.register(MarPrn)