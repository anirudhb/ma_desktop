def dec2bin(n):
        n = n
        b = ''
        while n:
                b = str(n % 2) + b
                n /= 2
        return b

def bin2dec(n):
        n = n
        sn = str(n)
        dec = 0
        strlen = len(sn)
        indexes = range(strlen, 0, -1)
        for ix in indexes:
                # print "%d: %d: sn[%d]: %s: %d" %(ix, strlen-ix, ix-1, sn[ix-1], (2 ** (strlen-ix)))
                dec += int(sn[ix-1]) * (2 ** (strlen-ix))
        return dec

# Place all your methods above this line so that they'll show up
dic = dir()

def main():
        from sys import argv as args
        import types
        try:
                args[1]
        except: 
                print "Methods available:", ', '.join([s for s in dic if not s.startswith("__") or not s.endswith("__")])
        else:
                try:
                        args[2]
                except:
                        import inspect
                        exec "print inspect.getsource(%s)" % args[1]
                        # print inspect.getsource(args[1])
                        return
                try:
                        args[3]
                except:
                        try:
                                exec "print %s(%s)" % (args[1], args[2])
                                # exec("print %s[%s.index(%s)](%s)" % (dic, dic, args[1], args[2]))
                        except:
                                try:
                                        args[4]
                                except:
                                        import inspect
                                        exec "print inspect.getsource(%s).split(\'\n\')[0]" % args[1]
                                else:
                                        exec "print %s(%s, %s)" % (args[1], args[2], args[3])
                
                

if __name__ == "__main__":
        main()
