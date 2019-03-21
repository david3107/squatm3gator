# -*- coding: utf-8 -*-
# Module to gather register date and check if it can find expiry date
import whois

class Whoiser:
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