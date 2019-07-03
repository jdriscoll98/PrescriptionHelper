from django import forms


class PrescriptionForm(forms.Form):
    name_of_medication = forms.CharField(max_length=100, required=True)
