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
Created on 04/02/2012

@author: mac@tid.es
'''

from sforce.enterprise import SforceEnterpriseClient

from os import environ

def connect():
    c = SforceEnterpriseClient(environ.get('SF_WSDL_PATH'))
    c.login(environ.get('SF_LOGIN'), environ.get('SF_PWD'), environ.get('SF_TOKEN'))
    
    return c

def update_contact(status, contact_id):
    
    c = connect()

    print c.retrieve('PaymentState__c', 'Contact', (contact_id))

    new_contact    = c.generateObject('Contact')
    new_contact.Id = contact_id

    new_contact.PaymentState__c = status

    c.update(new_contact)

    return True
