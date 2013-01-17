#!/usr/bin/python
# coding=utf-8 

'''
Created on 17/10/2012

@author: mac
'''

RECURRENT_PAYMENT_PAYLOAD = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE paymentService PUBLIC "-//WorldPay/DTD WorldPay PaymentService v1//EN" "http://dtd.worldpay.com/paymentService_v1.dtd">
    <paymentService version="1.4" merchantCode="%(merchantCode)s">
    <submit>
    <order orderCode="%(ordercode)s">
     <description>RECURRENT PAyment associated to First Order: %(lastordercode)s </description>
    <amount value="%(fillmoney)s" currencyCode="EUR" exponent="2" />
    <orderContent>TEST RECURRENT TEF PAYMENT ORDER %(lastordercode)s </orderContent>
    <payAsOrder orderCode="%(lastordercode)s" merchantCode="%(firstMerchantCode)s"> 
    <amount value="128" currencyCode="EUR" exponent="2" />
    </payAsOrder>
    </order>
    </submit>
    </paymentService>"""

FIRST_PAYMENT_PAYLOAD = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE paymentService PUBLIC "-//WorldPay/DTD WorldPay PaymentService v1//EN" "http://dtd.worldpay.com/paymentService_v1.dtd">
    <paymentService version="1.4" merchantCode="%(merchantCode)s">
    <submit>
    <order orderCode="%(ordercode)s">
     <description>TEST First Payment Order</description>
    <amount value="%(fillmoney)s" currencyCode="EUR" exponent="2" />
    <orderContent>TEST TEF PAYMENT ORDER V4444333322221111, MC5100080000000000 </orderContent>
    <paymentMethodMask>
    <include code="ALL"/>
    </paymentMethodMask>
    <shopper><shopperEmailAddress>globalbilling-internal@tid.es</shopperEmailAddress></shopper>
    <shippingAddress>
    <address>
    <firstName>Instant Server</firstName>
    <lastName>Telefonica Digital Online Channel</lastName>
    <address1>%(address)s</address1>
    <address2></address2>
    <address3></address3>
    <postalCode>%(postal_code)s</postalCode>
    <city>%(city)s</city>
    <countryCode>GB</countryCode>
    <telephoneNumber>0034686489600</telephoneNumber>
    </address>
    </shippingAddress>
    </order>
    </submit>
    </paymentService>"""

