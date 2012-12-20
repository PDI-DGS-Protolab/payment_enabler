'''
Created on 16/10/2012

@author: mac
'''

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)

    phone   = models.CharField(max_length = 10)
    title   = models.CharField(max_length = 10)
    company = models.CharField(max_length = 150)
    
    address     = models.CharField(max_length = 100)
    postal_code = models.CharField(max_length = 10)
    city        = models.CharField(max_length = 100)
    country     = models.CharField(max_length = 20)
    
    order_id = models.CharField(unique=True, max_length=10)