from socket import *
import time
import threading
# from socket import socket,AF_INET,SOCK_DGRAM
# import socket

shutdown = False
host = '127.0.0.1'
port = 4595
sc = ('localhost', 5000)
tlock = threading.Lock()
def receive(sock):
	while not shutdown:
		try:
			tlock.acquire()
			data, addr = sock.recvfrom(1024)
			data = data.decode()
			print str(data)
		except:
			pass
		finally:
			tlock.release()

com = socket(AF_INET, SOCK_DGRAM)
com.bind((host, port))
com.setblocking(0)
rT = threading.Thread(target=receive, args=[com])
rT.start()

name = raw_input('Name:')
msg = raw_input(name + '-> ')
while not shutdown:
	if msg == '/@server:sq:q':
		print('Server & client going down')
		msg = msg.encode()
		com.sendto('/@server:sq', sc)
		shutdown = True
		pass
	if msg == '/@p:q':
		print('Client going down')
		shutdown = True
		pass
	if msg == '/@server:sq':
		print('Server going down')
		com.sendto(msg, sc)
	if msg.startswith('/@/:') and msg != '':
		com.sendto(name.encode() + '>>> '.encode() + msg.encode(), sc)
	tlock.acquire()
	msg = raw_input(name + '-> ')
	tlock.release()
	time.sleep(2)

del name, msg, port, host, sc, tlock
rT.join()
com.close()

