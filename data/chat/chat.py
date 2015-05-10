from socket import *
import time, threading
#import socket
#from socket import AF_INET, socket, SOCK_DGRAM

def init():
    '''() -> NoneType

    
    Initalize the objects needed for use.
    '''
    global host
    global port
    global sc
    global coords
    host = '127.0.0.1'
    port = 0
    sc = (host, 5000)
    coords = [['host:', host],
              ['client port:', port],
              ['port:', 5000]]
    

def set_host(new_host):
    host = new_host

def set_server_port(new_port):
    sc = (host, new_port)

def set_port(new_port):
    port = new_port

def get_coords():
    try:
        print coords[0]
        print coords[1]
        print coords[2]
    except:
        return

class ChatServer(object):
    def __init__(self, name):
        import random
        self.name = name
        random.seed()
        self.id = random.randint(0, 1000000)
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind(sc)
        self.s.setblocking(0)
        self.clients = []
        
    def start(self):
        shutdown = False
        try:
            self.s
            print 'Server Started'
        except:
            print 'You don\'t have a socket object.\nYou cannot start the server.\nTry running __init__ again or delete and remake the object.\nTip: did you use quit()?\nA: You shouldn\'t.'
            return
        while not shutdown:
            try:
                import sys
                self.data, addr = self.s.recvfrom(1024)
                if self.data == 'Quit':
                    shutdown = True
                    if addr not in clients:
                        clients.append(addr)
                    for client in clients:
                        self.s.sendto('sq', client)
                    pass
                if addr not in self.clients:
                    self.clients.append(addr)
                print time.ctime(time.time()), ': :', data
                for client in clients:
                    self.s.sendto(data, client)
            except:
                pass

    def quit(self):
        self.s.close()
        del self.s, self.clients, self.id, self.name

            



class ChatClient(object):
    def __init__(self, name):
        import random
        random.seed()
        self.name = name
        self.id = random.randint(0, 5000)
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind((host, port))
        self.s.setblocking(0)
        self.tLock = threading.Lock()

    def recv(self):
        shutdown = False
        while not shutdown:
            try:
                self.data, addr = self.s.recvfrom(1024)
                if self.data == 'sq':
                    shutdown = True
                    pass
                print data
            except:
                pass
    def start(self):
        name = self.name
        msg = raw_input(name + '-> ')
        rT = threading.Thread(target=self.recv, args=[])
        rT.start()
        while msg != 'q':
            if msg != '':
                self.s.sendto(name + '>>> ' + data, sc)
            self.tLock.acquire()
            msg = raw_input(name + '-> ')
            self.tLock.release()
            time.sleep(0.2)
        rT.join()
        print 'quit/exit'

    def quit(self):
        del(self.recv)
        self.s.close()
        del self.id, self.name, self.s, self.id
        print 'Please delete the object.\nIt is now useless.'
