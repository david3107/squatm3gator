# -*- coding: utf-8 -*-
# Module to gather register date and check if it can find expiry date
import whois

class Whoiser:
	def __init__(self, url):
		self.url = url
		self.whois_info = whois.query(self.url)
		#print(self.whois_info.__dict__)

	def get_expiration_date(self):
		if self.whois_info is not None:
			return self.whois_info.expiration_date

	def get_creation_date(self):
		if self.whois_info is not None:
			return str(self.whois_info.creation_date)