#!/usr/bin/python
# coding=utf-8 

'''
Created on 16/10/2012

@author: mac
'''

from django.shortcuts           import render
from django.http                import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from payment.forms  import AcquireForm
from payment.models import UserProfile 

from wordpay.charger import Charger

import json

def acquire(request):
    
    if request.method == 'POST': 
        
        form = AcquireForm(request.POST) 
        
        if form.is_valid(): 
            
            # Only WorldPay at the moment
            charger = Charger()
            
            user = createUser(form)
            profile = createProfile(form, charger, user)
            
            url = charger.getRedirectUrl(profile)
            
            return HttpResponseRedirect(url)
    else:
        form = AcquireForm() 

    return render(request, 'acquire.html', {
        'form': form,
    })

def getCustomerDetails(request, contract):
    
    profiles = UserProfile.objects.filter(contract_id=contract)
    
    if (len(profiles) != 1):
        return HttpResponse(json.dumps({}), mimetype="application/json")
    
    profile = profiles[0]
    
    user = profile.user
    
    full_name = u'{0} {1}'.format(user.first_name, user.last_name)
    
    data =  {
            'name'       : full_name, 
            'address'    : user.address, 
            'city'       : user.city, 
            'postal_code': user.postal_code, 
            'email'      : user.email,
            'country'    : user.country
            }
    
    return HttpResponse(json.dumps(data), mimetype="application/json")

def createUser(acquireForm):
    username = getData(acquireForm, 'username')
    
    first_name  = getData(acquireForm, 'first_name')
    last_name   = getData(acquireForm, 'last_name')
    email       = getData(acquireForm, 'email')
    
    user = User(username=username, first_name=first_name, 
                last_name=last_name, email=email)
    
    user.save()
    
    return user

def createProfile(acquireForm, charger, user):
    
    title       = getData(acquireForm, 'title')
    
    phone       = getData(acquireForm, 'phone')
    company     = getData(acquireForm, 'company')
    
    address     = getData(acquireForm, 'address')
    postal_code = getData(acquireForm, 'postal_code')
    city        = getData(acquireForm, 'city')
    country     = getData(acquireForm, 'country')
       
    profile = UserProfile(user=user, phone=phone, company=company,
                          order_id=charger.getOrder(), 
                          title=title, address=address,
                          city=city, country=country,
                          postal_code=postal_code)
    profile.save()
    
    return profile

def getData(form, fieldname):
    return form.cleaned_data[fieldname]