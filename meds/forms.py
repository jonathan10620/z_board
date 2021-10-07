from django.forms import ModelForm
from .models import ScheduledMed


class ScheduledMedForm(ModelForm):
    class Meta:
        model = ScheduledMed
        fields = ["name", "dose", "frequency", "times"]
