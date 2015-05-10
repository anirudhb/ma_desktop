from socket import *

slist = []
for i in range(5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("localhost", 5000))
    slist.append(sock)

for sock in slist:
    sock.send("")
    sock.close()
