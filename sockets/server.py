from socket import *
import time

target = ("localhost", 5000)
s = socket(AF_INET, SOCK_STREAM)
s.bind(target)
s.listen(1)
client, addr = s.accept()
while 1:
    data = client.recv(1024)
    if data:
        print time.ctime(time.time()) + " : " + data
    else:
        break
s.close()
