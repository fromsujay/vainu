from django import forms
from .models import Locationdata
from django.core.exceptions import ValidationError

# This class creates the form for a user to generate location data
class LocationdataForm(forms.ModelForm):

# We import the field attributes from models.py file
    class Meta:
        model = Locationdata
        fields = '__all__'

# This function ensures that location name is lowercase
    def clean_locationid(self):
        return self.cleaned_data['locationid'].lower()
        
