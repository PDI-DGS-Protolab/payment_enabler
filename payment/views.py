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
    
    "Change this mock with the real data provided in the HTTP request"
    
    if request.method == 'POST':
        print "post"
        post = request.POST
        data = UserData(post.get('tef_account',None), post.get('city',None), post.get('address',None), 
                        post.get('postal_code',None), post.get('country',None), post.get('phone',None))
    else:
        return HttpResponse('<h1>Invalid Method</h1>',status=405)
    url = initial_payment_url(data)
    return HttpResponseRedirect(url)


def success(request):
    return render(request, 'success.html', {})

def pending(request):
    return render(request, 'pending.html', {})

def error(request):
    return render(request, 'error.html', {})
