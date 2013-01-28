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
Created on 17/10/2012

@author: mac@tid.es
'''

import urllib2

from BeautifulSoup import BeautifulSoup

from payloads import FIRST_PAYMENT_PAYLOAD, RECURRENT_PAYMENT_PAYLOAD
from payment_gateways.gateway_interface.PaymentGateway import PaymentGateway

class Worldpay_Charger (PaymentGateway):

    def __init__(self, model):
        
        self.RECURRENT_USERNAME = "GLOBALBILLINGEURREC"
        self.RECURRENT_PASSWORD = "xml2012launch"
        
        super(Worldpay_Charger, self).__init__(model)

    def get_response_document(self, xml, username, password):
        
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self.URL, username, password)

        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)

        headers = {
                    'Content-Type': "application/xml",
                    'Content-Length': len(xml)
                  }

        req = urllib2.Request(self.URL, xml, headers)

        try:
            f = opener.open(req)
            response_xml = f.read()

            print response_xml

            doc = BeautifulSoup(response_xml)

            return doc

        except urllib2.HTTPError, e:
            print "------------------Error------------------\n"
            print "Errortransaction. HTTP Error code:",e.code
            return None

    def get_redirect_url(self, user_data):
        
        xml = FIRST_PAYMENT_PAYLOAD % {
                                        "merchantCode" : self.USERNAME,
                                        "fillmoney": self.MONEY,
                                        "ordercode" : self.order,
                                        "city" : user_data.city,
                                        "address" : user_data.address,
                                        "postal_code" : user_data.postal_code,
                                        "country": user_data.country,
                                        "phone": user_data.phone
                                      }

        doc = self.get_response_document(xml, self.USERNAME, self.PASSWORD)

        if (not doc):
            return

        redirect_url = doc.find('reference').text

        finalUrl = "{0}&successURL={1}&pendingURL={2}&failureURL={3}".format(redirect_url, self.SUCCESS_CALLBACK,
                                                                             self.PENDING_CALLBACK, self.ERROR_CALLBACK)

        return finalUrl

    def recurrent_payment(self, order_data, master_info):

        order = order_data.order_code

        xml = RECURRENT_PAYMENT_PAYLOAD % {
                                            "merchantCode": self.RECURRENT_USERNAME,
                                            "fillmoney": order_data.total,
                                            "ordercode": order,
                                            "lastordercode": master_info.recurrent_order_code,
                                            "firstMerchantCode": self.USERNAME
                                            }

        doc = self.get_response_document(xml, self.RECURRENT_USERNAME, self.RECURRENT_PASSWORD)

        if (not doc):
            return

        print doc