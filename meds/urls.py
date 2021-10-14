from django.urls import path
from . import views


app_name = "meds"

urlpatterns = [
    # scheduled meds
    path("add/scheduled", views.add_schedule, name="add_sched"),
    path("detail/scheduled/<int:id>", views.detail_schedule, name="detail_sched"),
    path("delete/scheduled/<int:id>", views.delete_schedule, name="delete_sched"),
    # Prn Meds
    path("add/prn", views.add_prn, name="add_prn"),
    path("detail/prn/<int:id>", views.detail_prn, name="detail_prn"),
    path("delete/prn/<int:id>", views.delete_prn, name="delete_prn"),
]
