from django import forms
from datetime import date

class EquipmentForm(forms.Form):

    equipment_choices = [
        ("tubing", "cpap tubing"),
        ("headpiece", "headpiece"),
        ("blue_filter", "blue filter"),
        ("light_blue_filter", "light blue filter"),
        ("silicone_nose_piece", "silicone nose piece"),
        ("chamber", "chamber"),
        ("canister_&_Lids", "canister & lid"),
        ("filter", "suction filter"),
        ("catheter", "suction catheter"),
        ("G_Button", "g button"),
        ("GB_extension", "GB extension"),
        ]
    equipment = forms.ChoiceField(choices=equipment_choices, widget=forms.Select(attrs={'class': 'form-select form-control form-control-sm'}))

    date = forms.DateField(initial=date.today(),widget=forms.widgets.DateInput(attrs={'type': 'date', "class": "form-control form-control-sm"}))

    initials = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))