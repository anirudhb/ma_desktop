#!/usr/bin/python
from socket import *
import time
# import socket
# from socket import socket,AF_INET,SOCK_DGRAM


host = '127.0.0.1'
port = 5000
com = socket(AF_INET, SOCK_DGRAM)
com.connect((host, port))
com.setblocking(0)
clients = []


shutdown = False
print('Server Started.')
while not shutdown:
    try:
        data, addr = com.recvfrom(1024)
        if data == '/@server:sq':
            print 'Quit command received.\nServer going down.\nClosing connections and loops.\nTotal server shutdown initiated.\nq'
            shutdown = True
            pass
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            com.sendto(str(data), addr)
        print time.ctime(time.time()) + '@' + host + ': :' + str(data)
    except:
        pass
