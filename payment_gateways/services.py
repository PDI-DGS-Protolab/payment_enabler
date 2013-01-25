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

from models import PaymentGateway, MasterInformation, Order

import importlib

def initial_payment_url(user_data):
    country_code = user_data.country

    gws = PaymentGateway.objects.filter(country = country_code)

    if len(gws) == 0:
        return "/error"

    # If several, getting the first one
    gw = gws[0]

    charger = dynamically_loading_charger(gw)

    url = charger.get_redirect_url(user_data)

    store_master_information(user_data, charger.get_order(), gw)
    
    return url

def process_recurrent_payment(order_data):
    
    store_order(order_data)
    
    tef_account = order_data.tef_account
    country     = order_data.country

    master_infos = MasterInformation.objects.filter(tef_account=tef_account, gateway__country=country)

    if len(master_infos) == 0:
        return None

    # If several, getting the first one
    master_info = master_infos[0]
    
    gw = master_info.gateway
    
    charger = dynamically_loading_charger(gw)

    charger.recurrent_payment(order_data, master_info)
    
    return 1

def store_master_information(user_data, recurrent_order_code, gateway):
    master_info = MasterInformation (tef_account=user_data.tef_account, recurrent_order_code=recurrent_order_code, 
                                     gateway=gateway, email=user_data.email)
    master_info.save()

def store_order(order_data):
    order = Order(total=order_data.total, currency=order_data.currency, country=order_data.country,
                  tef_account=order_data.tef_account, statement=order_data.statement, 
                  order_code=order_data.order_code)
    
    order.save()

def dynamically_loading_charger(gw):
    charger_module = importlib.import_module(gw.module_name)
    charger = getattr(charger_module, gw.class_name)(gw)
    
    return charger