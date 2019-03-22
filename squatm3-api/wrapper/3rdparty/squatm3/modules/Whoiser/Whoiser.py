# -*- coding: utf-8 -*-
# Module to gather register date and check if it can find expiry date
import whois

class Whoiser:
<<<<<<< HEAD
	def __init__(self):
		self.domain = ""
		self.expiration_date = ""
		self.creation_date = ""

	def get_info(self, domain):
		self.domain = domain
		self.expiration_date = ""
		self.creation_date = ""
		w = whois.query(self.domain)
		if w is not None:
			if w.expiration_date is not None:
				self.expiration_date = str(w.expiration_date.strftime("%d.%m.%Y %H:%M:%S"))
			if w.creation_date is not None:
				self.creation_date = str(w.creation_date.strftime("%d.%m.%Y %H:%M:%S"))
=======
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
>>>>>>> e4b3e66e5df9733e31e4a4ca4d05dac370e315f9
