from django import forms
from datetime import datetime
from django.utils import timezone
from .models import Seizure


class SeizureForm(forms.ModelForm):
    def no_future_date(value):
        if value > timezone.now():
            raise forms.ValidationError("Date and time cannot be in the future")
    date = forms.DateTimeField(validators=[no_future_date],widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control form-control-sm"}))
    action = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm", 'placeholder': 'Med/Intervention'})
    )
    initial = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )

    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Seconds'}))

    def __init__(self, *args, **kwargs):
        super(SeizureForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.today().strftime('%Y-%m-%dT%H:%M')
        

    class Meta:
        model = Seizure
        fields = ['date', 'duration', 'action', 'initial']