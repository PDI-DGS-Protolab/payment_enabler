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
Created on 30/10/2012

@author: mac@tid.es
'''

from payment.models import PaymentGateway

from models import Order

import importlib

def initial_payment_url(payment_data):
    country_code = payment_data.country

    gws = PaymentGateway.objects.filter(country = country_code)

    if len(gws) == 0:
        return "/error"

    # If several, getting the first one
    gw = gws[0]

    charger_module = importlib.import_module(gw.module_name)
    
    charger = getattr(charger_module, gw.class_name)(gw)

    url = charger.get_redirect_url(payment_data)

    store_order_details(payment_data.tef_account, charger.get_order(), gw)
    
    return url

def store_order_details(tef_account, order_id, gateway):
    order = Order(tef_account=tef_account, order=order_id, gateway=gateway)
    order.save()