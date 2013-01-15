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
from django.views.decorators.csrf   import csrf_exempt
from django.http                    import HttpResponse
from django.shortcuts               import render
from django.http                    import HttpResponseRedirect
from django.db                      import transaction

from services import initial_payment_url
from api_format import UserData

@csrf_exempt
@transaction.commit_on_success
def initial_payment(request):
    
    if request.method == 'POST':

        post = request.POST
        data = UserData(post.get('tef_account',"tefaccount111"), post.get('city', "Madrid"),
                        post.get('address', "Calle de la Hoz"), post.get('postal_code', "29332"),
                        post.get('country', "Spain"), post.get('phone', "939393939"),
                        post.get('email', "mac@tid.es"))
    else:
        return HttpResponse('<h1>Invalid Method</h1>', status=405)

    url = initial_payment_url(data)
    return HttpResponseRedirect(url)

def payment_info(request):
    return render(request, 'payment_info.html', {})

