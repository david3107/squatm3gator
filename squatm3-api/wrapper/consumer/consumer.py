import redis, os, subprocess
from wrapper.classes import job, comm, utils

worker_id = utils.generate_global_uuid()
c_jobs = comm.Communication()
job_process = None

def report(connection, channel, message):
	#connection.redis.lpush(connection.channel_reporting, message)
	if channel == connection.channel_reporting:
		connection.redis.lpush(connection.channel_reporting, message)
	elif channel ==  connection.channel_debug:
		connection.redis.lpush(connection.channel_debug, message)
	elif channel == connection.channel_jobs:
		connection.redis.lpush(connection.channel_jobs, message)

def process(new_job):
	global job_process
	if isinstance(new_job, job.Job):
		#Process job
		try:
			if new_job.command == "ENUMERATE":
				if job_process is not None and job_process.poll() is None:
					report(c_jobs, c_jobs.channel_debug, worker_id + "# ALREADY IN ATTACK")
					return
				report(c_jobs, c_jobs.channel_debug, worker_id + '#' + new_job.id + "# started attack job:" + new_job.url)
				
				job_process = subprocess.Popen("python3 wrapper/3rdparty/squatm3/squatme.py --url " + new_job.url + " " + new_job.options, 
					shell=True, stdout=subprocess.PIPE)
				while job_process.poll() is None:
					output = job_process.stdout.readline()
					if len(output)>1:
						report(c_jobs, c_jobs.channel_reporting, worker_id + '#' + new_job.id + "# " + output.decode().strip())
					

			elif new_job.command == "STOP":
				report(c_jobs, c_jobs.channel_debug, worker_id + '#' + new_job.id + "# STOP ENUMERATION: " + new_job.id)
				if job_process is not None and job_process.poll() is None:
					print("killing the attack pid")
					job_process.kill()
					report(c_jobs, c_jobs.channel_debug, worker_id + '#' + new_job.id + "# ENUMERATION STOPPED: " + new_job.id)
					job_process = None
			else:
				report(c_jobs, c_jobs.channel_debug, worker_id + '#' + new_job.id + "# unknown command")
		except:
				report(c_jobs, c_jobs.channel_debug, worker_id + '#' + new_job.id + "# error procesing job")

def listen_for_commands():
	pubsub_jobs = c_jobs.redis.pubsub(ignore_subscribe_messages=True)
	pubsub_jobs.subscribe(c_jobs.channel_jobs)
	#listen for enumeration tasks
	while True:
		a_json_string = pubsub_jobs.get_message()
		if a_json_string:
			new_job = job.Job()
			json_string = a_json_string["data"].decode("utf-8") 
			new_job.from_json(json_string)
			process(new_job)

		

def start_reporting():
	c = comm.Communication()
	while True:
		job = c.redis.rpop(c.channel_reporting)
		if job:
			print(job)

if __name__ == "__main__":
    pass