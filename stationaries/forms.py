from django import forms
from .models import Stationaries, StationaryActivity


class StationaryActivityForm(forms.ModelForm):
    class Meta:
        model = StationaryActivity
        fields = ['stationary', 'stationary_count', 'price', 'comment']
