'''
Created on 17/10/2012

@author: mac
'''

import uuid

class PaymentGateway:
    
    def getRedirectUrl(self, profile):
        pass

    def recurrentPayment(self, lastOrder, total):
        pass

    def getOrder(self):
        return self.order
    
    def computeOrderId(self):
        uid = uuid.uuid4()
        
        # Order = ten first characters of uuid
        return uid.hex[:10]