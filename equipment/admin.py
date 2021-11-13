from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CPAP)
admin.site.register(models.Other)
admin.site.register(models.Suction)
