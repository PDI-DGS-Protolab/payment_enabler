#!/usr/bin/python
# coding=utf-8 

import urllib2

from BeautifulSoup import BeautifulSoup

from payment.wordpay.payloads import FIRST_PAYMENT_PAYLOAD, RECURRENT_PAYMENT_PAYLOAD
from payment.gateway_interface.PaymentGateway import PaymentGateway

class Charger (PaymentGateway):

	URL = "https://secure-test.worldpay.com/jsp/merchant/xml/paymentService.jsp"
	
	USERNAME = "GLOBALBILLINGEUR"
	PASSWORD = "xml2012launch"
	
	RECURRENT_USERNAME = "GLOBALBILLINGEURREC"
	RECURRENT_PASSWORD = "xml2012launch"
	
	MONEY = 128
	
	def __init__(self):
		self.order = self.computeOrderId()
		
	def getResponseDocument(self, xml, username, password):
		
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
			responseXml = f.read()
			
			print responseXml
			
			doc = BeautifulSoup(responseXml)
			
			return doc
			
		except urllib2.HTTPError, e:
			print "------------------Error------------------\n"
			print "Errortransaction. HTTP Error code:",e.code
			return None
	
	def getRedirectUrl(self, profile):
		
		xml = FIRST_PAYMENT_PAYLOAD % {
										"merchantCode" : self.USERNAME, 
										"fillmoney": self.MONEY, 
										"ordercode" : self.order,
										"city" : profile.city,
										"address" : profile.address,
										"postal_code" : profile.postal_code
									  }
		
		doc = self.getResponseDocument(xml, self.USERNAME, self.PASSWORD)
		
		if (not doc):
			return

		redirectUrl = doc.find('reference').text
			
		return redirectUrl

	def getOrder(self):
		return self.order

	def recurrentPayment(self, lastOrder, total):
		
		order = self.computeOrderId()
		
		xml = RECURRENT_PAYMENT_PAYLOAD % {
											"merchantCode": self.RECURRENT_USERNAME, 
											"fillmoney": total, 
											"ordercode": order, 
											"lastordercode": lastOrder, 
											"firstMerchantCode": self.USERNAME
											}
		
		doc = self.getResponseDocument(xml, self.RECURRENT_USERNAME, self.RECURRENT_PASSWORD)
		
		if (not doc):
			return
		
		print doc