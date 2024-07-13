from django import forms
from django.forms import ModelForm
from .models import Led


class ledForm(ModelForm):
    class Meta:
        model = Led
        fields = ('title', 'time_on', 'time_off', 'simulation_time')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control' }),
            'time_on': forms.NumberInput(attrs={'class': 'form-control' }),
            'time_off': forms.NumberInput(attrs={'class': 'form-control' }),
            'simulation_time': forms.NumberInput(attrs={'class': 'form-control' }),
        }

    


