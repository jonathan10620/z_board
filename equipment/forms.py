from django import forms
from datetime import date

def no_future_date(value):
    if value > date.today():
        raise forms.ValidationError("Date cannot be in the future")


class EquipmentForm(forms.Form):

    equipment_choices = [
        # cpap items
        ("Tubing", "cpap tubing"),
        ("Headpiece", "headpiece"),
        ("Blue filter", "blue filter"),
        ("Light blue filter", "light blue filter"),
        ("Silicone nose piece", "silicone nose piece"),

        # suction items
        ("Chamber", "Suction chamber"),
        ("Canister & Lids", "canister & lid"),
        ("Filter", "suction filter"),
        ("Catheter", "suction catheter"),

        # other items
        ("G Button", "g button"),
        ("GB extension", "GB extension"),
        ]
    equipment = forms.ChoiceField(choices=equipment_choices, widget=forms.Select(attrs={'class': 'form-select form-control form-control-sm'}))

    date = forms.DateField(validators=[no_future_date],initial=date.today(),widget=forms.widgets.DateInput(attrs={'type': 'date', "class": "form-control form-control-sm"}))

    initials = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))