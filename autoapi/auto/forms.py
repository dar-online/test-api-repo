from django import forms
from auto.models import *

class CarAddForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('price', 'year', 'name', 'car_marka', 'car_model')
