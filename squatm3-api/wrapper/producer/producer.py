import redis
from wrapper.classes import comm

c = comm.Communication()
c.pubsub = c.redis.pubsub()

def publish(channel, object):
	c.redis.publish(channel, object)

def push(channel, object):
	c.redis.lpush(channel, object)

if __name__ == "__main__":
    pass

