from django.forms import ModelForm
from service import models
from stationaries.models import StationaryActivity


class EditActivityForm(ModelForm):
    class Meta:
        model = models.Activity
        fields = ['service', 'service_count', 'price', 'comment']


class EditCustomActivityForm(ModelForm):
    class Meta:
        model = models.CustomActivity
        fields = ['service', 'service_count', 'price', 'comment']


class EditStationaryActivityForm(ModelForm):
    class Meta:
        model = StationaryActivity
        fields = ['stationary', 'stationary_count', 'price', 'comment']