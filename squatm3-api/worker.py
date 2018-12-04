import redis
from wrapper.classes import job
from wrapper.consumer import consumer

c = consumer
c.listen_for_commands()