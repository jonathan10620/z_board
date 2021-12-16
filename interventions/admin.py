from django.contrib import admin

from .models import BreathingEntry, FeedingEntries

# Register your models here.

admin.site.register(FeedingEntries)
admin.site.register(BreathingEntry)