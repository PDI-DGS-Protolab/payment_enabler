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
Created on 14/01/2013

@author: mac@tid.es
'''


from datetime import datetime

from payment.gateway_interface.PaymentGateway import PaymentGateway
from py_adyen.adyen import Adyen
from py_adyen.api import Api

class Adyen_Charger (PaymentGateway):

    def __init__(self, model):
        super(Adyen_Charger, self).__init__(model)

    def get_response_document(self, xml, username, password):
        pass

    def get_redirect_url(self, user_data):

        data = {
            'merchantReference': '1337',           # your internal reference for this payment
            'paymentAmount': self.MONEY,
            'currencyCode': self.CURRENCY,
            'shipBeforeDate': datetime.now(),
            'shopperEmail': 'foobar@example.com',  # useful for recurring payments etc.
            'shopperReference': user_data.tef_account,         # your internal reference for (recurring) lookups etc.
            'sessionValidity': datetime.now(),     # how long is the payment session valid
            'recurringContract': 'RECURRING',     # Mark this authorisation for recurring payments
        }

        a = Adyen(data)
        a.sign()

        form = a.get_form()

#        ws = Api()
#
#        statement = 'Subscription Fee October'  # public payment statement for user
#        reference = self.get_order()
#
#        shopper_email     = user_data.email
#        shopper_reference = user_data.tef_account
#
#        amount   = self.MONEY
#        currency = self.CURRENCY
#
#        ws.authorise_recurring_payment(reference, statement, amount, currency, shopper_reference, shopper_email,
#                                       shopper_ip=None, recurring_detail_reference='LATEST')

        return a.get_redirect_url()



    # total must be a float formatted to two decimal points
    def recurrent_payment(self, lastOrder, total):
        pass
