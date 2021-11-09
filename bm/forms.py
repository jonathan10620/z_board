from django import forms
from .models import BM

from datetime import datetime

class BMForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control form-control-sm"}))
    comment = forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )

    initial = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )

    size = forms.ChoiceField(choices=BM.bm_sizes,
        widget=forms.Select(attrs={'class': 'form-select form-control form-control-sm'})
        # `ModelChoiceField` is using the `Select` widget bu default
    )

    def __init__(self, *args, **kwargs):
        super(BMForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.today().strftime('%Y-%m-%dT%H:%M')
        

    class Meta:
        model = BM
        fields = ['size', 'date', 'comment', 'initial']