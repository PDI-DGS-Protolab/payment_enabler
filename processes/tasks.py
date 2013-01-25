#!/usr/bin/python
#coding=utf-8 

"""
Copyright 2013 Telefonica Investigación y Desarrollo, S.A.U

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
Created on 25/01/2013

@author: mac@tid.es
'''


from celery import task

######################################################
# PAYMENT DATA ACQUISITION TASKS
######################################################

@task(ignore_result=True)
def notify_salesforce_task(state):
    pass

######################################################
# PAYMENT DATA ACQUISITION PROCESS
######################################################

def start_notify_salesforce(state):
    chain = notify_salesforce_task.s(state) 
            
    chain()

def sync_notify_salesforce(state):
    notify_salesforce_task(state)

######################################################
# RECURRENT CHARGING TASKS
######################################################

@task(ignore_result=True)
def payment_gateway_invocation_task(charging_result):
    return charging_result

@task(ignore_result=True)
def notify_backoffice_task(json):
    return json

######################################################
# RECURRENT CHARGING PROCESSES
######################################################

def start_invoke_gateway(json):
    chain = payment_gateway_invocation_task.s(json)

    chain()

def start_notify_backoffice(json):
    chain = notify_backoffice_task.s(json)

    chain()