from django.forms.widgets import Select
from .models import *
from django import forms

# gender = forms.CharField(label='gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))


class BloodDonorForm(forms.ModelForm):
    class Meta:
        model = BloodDonor
        fields = '__all__'
        labels={
            'name':'',
            'age':'',
            'gender':'',
            'city':'',
            'phonenumber':''
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter Your Name'}),
            'age':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter Your Age'}),
            'gender':forms.RadioSelect(choices=GENDER_CHOICES),
            'blood_group':forms.Select(attrs={'class':'form-select sel'}),
            'city':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter Your city'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter Your Mobile No.'}),
            
        }
