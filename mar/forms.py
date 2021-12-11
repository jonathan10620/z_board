from datetime import datetime

from django import forms

from meds.models import PrnMed

from .models import MarPrn


class PrnMarForm(forms.ModelForm):
    mar_datetime = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', "class": "form-control form-control-sm"}))
    indication = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    initial = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    med = forms.ModelChoiceField(
        queryset=PrnMed.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select form-control form-control-sm'})
        # `ModelChoiceField` is using the `Select` widget bu default

    )

    def __init__(self, *args, **kwargs):
        super(PrnMarForm, self).__init__(*args, **kwargs)
        print(f'{datetime.today()} _________')
        self.fields['mar_datetime'].initial = datetime.today().strftime('%Y-%m-%dT%H:%M')
        

    class Meta:
        model = MarPrn
        fields = ['med', 'mar_datetime', 'indication', 'initial']