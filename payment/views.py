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

from django.http                    import HttpResponse
from django.shortcuts               import render
from django.http                    import HttpResponseRedirect
from django.db                      import transaction

from services   import initial_payment_url
from api_format import UserData


@transaction.commit_on_success
def initial_payment(request):

    if request.method == 'POST':

        params = request.POST.get

        tef_account = params('tef_account', None)
        city        = params('city', None)
        address     = params('address', None)
        postal_code = params('postal_code', None)
        country     = params('country', None)
        phone       = params('phone', None)
        email       = params('email', None)

        if (not tef_account or not city or not address or not postal_code or
            not country or not phone or not email):
            return HttpResponse('<h1>Insufficient parameters!</h1>', status=405)

        data = UserData(tef_account, city, address, postal_code, country, phone, email)
    else:
        return HttpResponse('<h1>Invalid Method</h1>', status=405)

    url = initial_payment_url(data)
    
    return HttpResponseRedirect(url)

def payment_info(request):

    if request.method == 'GET':

        params = request.GET.get

        tef_account = params('tef_account', "1928jj2js")
        city        = params('city', "dummy_city")
        address     = params('address', "dummy_address")
        postal_code = params('postal_code', "28373")
        country     = params('country', "ES")
        phone       = params('phone', "947373737")
        email       = params('email', "mac@tid.es")

        context = {
                   'tef_account': tef_account,
                   'city':        city,
                   'address':     address,
                   'postal_code': postal_code,
                   'country':     country,
                   'phone':       phone,
                   'email':       email
                  }


        return render(request, 'payment_info.html', context)
    else:
        return HttpResponse('<h1>Invalid Method</h1>', status=405)

