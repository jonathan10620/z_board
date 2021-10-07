from django.urls import path
from . import views


app_name = "meds"

urlpatterns = [
    path("add", views.addmed, name="addmed"),
]
