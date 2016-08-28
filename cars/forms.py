from django import forms
from django.core.exceptions import ValidationError

from .models import Car_var, Person


class AddNewCarForm(forms.ModelForm):
    class Meta:
        model = Car_var
        fields = ('const_vin',)
    registration_no = forms.CharField(choices=(
        ('jeden', '1'),
        ('dwa', '2'),
        ()))
