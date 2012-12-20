#!/usr/bin/python
#coding=utf-8 

"""
Copyright 2012 Telefonica Investigación y Desarrollo, S.A.U

This file is part of Billing_PoC.

Billing_PoC is free software: you can redistribute it and/or modify it under the terms 
of the GNU Affero General Public License as published by the Free Software Foundation, either 
version 3 of the License, or (at your option) any later version.
Billing_PoC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero 
General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with Billing_PoC. 
If not, see http://www.gnu.org/licenses/.

For those usages not covered by the GNU Affero General Public License please contact with::mac@tid.es
""" 

'''
Created on 16/10/2012

@author: mac@tid.es
'''

from django import forms

COUNTRIES = (
             ('Spain', 'Spain'),
            )

TITLES = (
          ('Mr', 'Mr'),
          ('Miss', 'Miss'),
          ('Mrs', 'Mrs'),
          ('Dr', 'Dr'),
         )

COUNTRIES_CODE = {
                  'Spain': 'ES'
                  }

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