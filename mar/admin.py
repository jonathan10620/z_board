from django.contrib import admin
from .models import MarScheduled, MarPrn

# Register your models here.
admin.site.register(MarScheduled)
admin.site.register(MarPrn)