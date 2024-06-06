from django import forms
from django.forms import ModelForm
from .models import Led


class ledForm(ModelForm):
    class Meta:
        model = Led
        fields = ('title', 'time_on', 'time_off', 'simulation_time', 'key')

    


