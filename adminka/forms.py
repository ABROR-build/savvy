from django.forms import ModelForm
from service import models


class EditActivityForm(ModelForm):
    class Meta:
        model = models.Activity
        fields = ['service', 'service_count', 'price', 'comment']


class EditCustomActivityForm(ModelForm):
    class Meta:
        model = models.CustomActivity
        fields = ['service', 'service_count', 'price', 'comment']