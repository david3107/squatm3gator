import attr, uuid, json
from wrapper.classes import utils

@attr.s
class Job:
	def to_json(self):
		return json.dumps(attr.asdict(self))

	def from_json(self, json_string):
		json_string = json.loads(json_string)
		self.id = json_string["id"]
		self.command = json_string["command"]
		self.url = json_string["url"]
		self.options = json_string["options"]

	id = attr.ib(default=utils.generate_global_uuid())
	url =  attr.ib(default="")
	command = attr.ib(default="ENUMERATE") #or stop to stop attack
	options = attr.ib(default="--help")

