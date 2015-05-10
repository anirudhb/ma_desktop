import time

class Timer:
    def __init__(self, limit, resttime):
        self.limit = limit
        self.resttime = resttime
        self.fhandle = open("stime", "r+")
        self.mxhandle = open("dtime", "r+")

    def start(self, finishfunction):
        self.fhandle.write(str(int(time.time())))
        self.fhandle.seek(0)
        self.mxhandle.write(str(int(time.time()))
        self.mxhandle.seek(0)
        t = int(self.fhandle.read().strip("\n"))
        self.maxtime = t+self.limit
        while t != self.maxtime:
            self.fhandle.seek(0)
            self.fhandle.write(str(int(time.time())))
            self.fhandle.seek(0)
            t = int(self.fhandle.read().strip("\n"))
        self.maxtime = t+self.resttime
        t = int(self.mxhandle.read().strip("\n"))
        while t != self.maxtime:
            finishfunction()
            self.mxhandle.seek(0)
            self.mxhandle.write(str(int(time.time())))
            self.mxhandle.seek(0)
            t = int(self.mxhandle.read().strip("\n"))
            
