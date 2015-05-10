from socket import *
import time

target = ("localhost", 5000)
s = socket(AF_INET, SOCK_STREAM)
s.connect(target)
name = raw_input("Name: ")
data = raw_input(name+"> ")
while data:
    if not data:
        s.send(data)
    else:
        s.send(name+" : "+data)
    print s.recv(1024)
    data = raw_input(name+"> ")

s.close()
