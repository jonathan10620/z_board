from .models import FeedingEntries
from django import forms

class FeedingForm(forms.ModelForm):
    class Meta:
        model = FeedingEntries
        fields = '__all__'