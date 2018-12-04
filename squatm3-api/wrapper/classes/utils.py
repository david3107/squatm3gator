import uuid
import socket
import fcntl
import struct

def get_address_of_interface(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_address():
	return socket.gethostbyname(socket.gethostname())

def generate_global_uuid():
	return str(uuid.uuid4())