import socket
import time
hosts = []
def broadcast(op):
	#broadcast your ip, should put in a timed loop
	while True:
		bsock=socket(socket.AF_INET, socket.SOCK_DGRAM)
		bsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		bsock.sendto(uname + ' at ' +  ,("192.168.0.255",12345))
		if str(op) != "once":
			time.sleep(120)
		else:
			bsock.close()
			break()

def listen():
	#listen to broadcast for hosts. 
	while True:
		s=socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(('192.168.0.109', 12345))
		s.listen(1)
		message=s.recvfrom(1024)
		if str(message) == "asking":
			broadcast(once)
		else:
			hosts.append(message)

		#should put in an array of hosts
def startup():
	broadcast()
	listen():
	ask():
	uname = raw_input("what is your username?")
def ask():
	bsock=socket(socket.AF_INET, socket.SOCK_DGRAM)
	bsock.sendto("asking",("192.168.0.255",12345))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("starting up on %s" % server_address)
startup()
if len(hosts) > 0:
	print("Hosts Found!")
	print(hosts)













#print(str(socket.gethostbyname(socket.getfqdn())))