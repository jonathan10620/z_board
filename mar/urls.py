from django.urls import path
from . import views


app_name = "mar"

urlpatterns = [
    path("scheduled", views.scheduled, name="scheduled"),
    path("prn", views.prn, name="prn"),
]
