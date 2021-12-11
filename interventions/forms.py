from datetime import datetime

from django import forms

from .models import FeedingEntries


class FeedingForm(forms.ModelForm):
    time_given = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time',"class": "form-control form-control-sm"},format='%H:%M'))

    initials = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )

    def __init__(self, *args, **kwargs):
        super(FeedingForm, self).__init__(*args, **kwargs)
        self.fields['time_given'].initial = datetime.now().strftime('%H:%M')

    feeding_choice = forms.CharField(required=False)
    day = forms.CharField(required=False)

    class Meta:
        model = FeedingEntries
        fields = '__all__'
    