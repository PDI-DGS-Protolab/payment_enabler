#!/usr/bin/python
# coding=utf-8 

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

from django.shortcuts import render
from django.http      import HttpResponseRedirect
from django.db        import transaction

from services import initial_payment_url
from api_format import UserData

@transaction.commit_on_success
def initial_payment(request):

    "Change this mock with the real data provided in the HTTP request"
    data = UserData("tefaccount111", "Madrid", "Calle de la Hoz", "29332", "Spain", "939393939", "mac@tid.es")
                        
    url = initial_payment_url(data)
            
    return HttpResponseRedirect(url)

def payment_info(request):
    return render(request, 'payment_info.html', {})
