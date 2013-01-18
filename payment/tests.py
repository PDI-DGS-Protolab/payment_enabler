#!/usr/bin/python
#coding=utf-8 

"""
Copyright 2012 Telefonica Investigacion y Desarrollo, S.A.U

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

"""
Created on 16/01/2013

@author: mac@tid.es
"""

import manage

# Loading environment variables prior to initialice django framework
manage.read_env('../.env')

from django.test import TestCase

from payment.api_format import OrderData, UserData
from payment.models import PaymentGateway
from payment.adyen.adyen_charger import Adyen_Charger

class TestGenerator(TestCase):
    
    def test_adyen_recurrent_payment(self):
        
        order_data = OrderData(total=500, currency="EUR", recurrent_order="", statement="Testing statement")
        user_data  = UserData(tef_account="tefaccount111", city="", address="", postal_code="",
                              country="", phone="", email="foobar@example.com")
        
        gw_data = PaymentGateway.objects.get(name="ADYEN")
        
        adyen_charger = Adyen_Charger(gw_data)
        
        adyen_charger.recurrent_payment(order_data, user_data)
