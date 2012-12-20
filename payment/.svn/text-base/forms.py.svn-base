'''
Created on 16/10/2012

@author: mac
'''

from django import forms

COUNTRIES = (
             ('ES', 'Spain'),
            )

TITLES = (
          ('Mr', 'Mr'),
          ('Miss', 'Miss'),
          ('Mrs', 'Mrs'),
          ('Dr', 'Dr'),
         )

class AcquireForm(forms.Form):
    username   = forms.CharField(max_length=30, min_length=3)
    
    title = forms.ChoiceField(choices=TITLES, widget=forms.Select(attrs={'class':'selector'}))
    
    first_name = forms.CharField(max_length=30, min_length=3)
    last_name  = forms.CharField(max_length=30, min_length=3)
    
    email    = forms.EmailField(max_length = 30, min_length=6)
    email2   = forms.EmailField(max_length = 30, min_length=6, label="Confirm email")
    
    company = forms.CharField(max_length=150, min_length=3)
    
    address     = forms.CharField(max_length=100, min_length=3)
    postal_code = forms.CharField(max_length=10, min_length=3)
    city        = forms.CharField(max_length=100, min_length=2)
    country     = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={'class':'selector'}))
    
    phone   = forms.CharField(max_length = 10, min_length=9)
    
    def clean_email(self):
        email  = self.data['email']
        email2 = self.data['email2']
        
        if (email != email2):
            raise forms.ValidationError("Emails must match")

        return email