import redis, attr, json
from classes import job, comm
from producer import producer

c = comm.Communication()
p = producer

#create attack
j = job.Job("www.asdasd.com")
#options
j.options = "-Hf --output=json"
#command
p.publish(c.channel_jobs, j.to_json())

#send command
#cmd = command.Command()
#cmd.command = "STOP_ATTACK"
#p.publish(c.channel_warriors, cmd.to_json())