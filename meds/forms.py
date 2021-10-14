from django import forms


class ScheduledMedForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    dose = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    frequency = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    times = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )


class PrnMedForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    dose = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
    indication = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"})
    )
