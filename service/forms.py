from django import forms
from .models import Activity, CustomActivity, Services


class ActivityForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Services.objects.all())
    class Meta:
        model = Activity
        fields = ['service', 'service_count', 'price', 'comment']


class CustomActivityForm(forms.ModelForm):
    class Meta:
        model = CustomActivity
        fields = ['service', 'service_count', 'price', 'comment']
