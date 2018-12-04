import redis, attr

@attr.s
class Communication:

	def build_connection():
		return redis.Redis(
	  	    host='localhost',
	    	port=6379,
	    	password='waddup')
	
	def config_reporting_channel():
		#TODO: read from config file
		return "squatm3.reporting"

	def config_debug_channel():
		#TODO: read from config file
		return "squatm3.debug"

	def config_jobs_channel():
		#TODO: read from config file
		return "squatm3.job"

	redis = attr.ib(default=build_connection())

	channel_reporting = attr.ib(default=config_reporting_channel())
	channel_debug = attr.ib(default=config_debug_channel())
	channel_jobs = attr.ib(default=config_jobs_channel())
