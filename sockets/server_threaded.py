from socket import *
from threading import Thread, Lock
import time
import sys

tlock = Lock()
target = ("localhost", 5000)
s = socket(AF_INET, SOCK_STREAM)
s.bind(target)
s.listen(5)

def client_handler():
    client, addr = s.accept()
    while 1:
        data = client.recv(1024)
        if not data:
            sys.exit(0)
        print time.ctime(time.time()) + " : " + data
        try:
            tlock.acquire()
            s.send(data)
            tlock.release()
        except:
            pass

for i in range(5):
    Thread(target=client_handler).start()

s.close()
