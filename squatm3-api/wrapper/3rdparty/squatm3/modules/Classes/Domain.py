# -*- coding: utf-8 -*-
import simplejson
class Domain:
	def __init__(self):
		self.fqdn = ""
		self.purchasable = None
		self.price = ""
		self.no_info = False
		self.creation_date = ""
<<<<<<< HEAD
		self.expiration_date = ""
=======
		self.expiry_date = ""
>>>>>>> e4b3e66e5df9733e31e4a4ca4d05dac370e315f9

	def _asdict(self):
		return self.__dict__

	def toJSON(self):
		return simplejson.dumps(self.__dict__, ensure_ascii=False)