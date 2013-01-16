#!/usr/bin/python
#coding=utf-8 

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

from django.contrib.auth.models import User
from django.db import models

COUNTRIES_CODE = {
    'Spain': 'ES'
}



class PaymentGateway(models.Model):

    name = models.CharField(max_length = 100)

    endpoint = models.CharField(max_length = 200)

    success_callback = models.CharField(max_length = 200)
    error_callback   = models.CharField(max_length = 200)
    pending_callback = models.CharField(max_length = 200)

    merchant = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

    class_name = models.CharField(max_length = 50)

class Order(models.Model):

    gateway     = models.ForeignKey(PaymentGateway)
    tef_account = models.CharField(max_length = 20)
    order       = models.CharField(unique=True, max_length=10)

    STATUS = (
        ('PENDING',   'PENDING'),
        ('VALIDATED', 'VALIDATED'),
        ('ERROR',     'ERROR'),
        ('CANCELED',  'CANCELED'),
    )

    status = models.CharField(max_length=10, choices=STATUS, default='PENDING')

class PaymentProcess(models.Model):

    bo_process_id = models.IntegerField(null=True)
    callback      = models.CharField(max_length = 200, null=True)

    tef_account = models.CharField(max_length = 20)
    amount      = models.IntegerField()
    currency    = models.IntegerField()
    country     = models.IntegerField()

    result = models.TextField()