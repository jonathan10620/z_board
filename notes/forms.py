from django import forms
from .models import Note
from datetime import datetime
from django.utils import timezone


class NoteForm(forms.ModelForm):
    def no_future_date(value):
        if value > timezone.now():
            raise forms.ValidationError("Date and time cannot be in the future")

    date = forms.DateTimeField(
        validators=[no_future_date],
        widget=forms.widgets.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control form-control-sm"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3"})
    )

    author = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields["date"].initial = datetime.today().strftime("%Y-%m-%dT%H:%M")

    class Meta:
        model = Note
        fields = ["date", "body", "author"]
