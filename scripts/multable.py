#!/usr/bin/env python
# Multiplication Fact Table

##def multable(n1, n2:
##        i = n1
##        i2 = 1
##        for ix in range(n2):
##                print i, "X", i2, "=", i*i2
##                i2 += 1
##
##def negmultable(neg1, neg2):
##        i = neg1
##        if neg2 > 0:
##                i2 = 1
##        if neg2 < 0:
##                i2 = -1
##        while 1:
##                print i, "X", i2, "=", i*i2
##                if i2 == neg2:
##                        break
##                if neg2 < 0:
##                        i2 += -1
##                if neg2 > 0:
##                        i2 += 1

def multable(n1, n2):
        for i in range(1, n2+1):
                print "{0} X {1} = {2} {1}".format(n1, i, n1*i)

def negmultable(n1, n2):
        for i in range(-1, n2-1, -1):
                print "{0} X {1} = {2}".format(n1, i, n1*i)

def main():
        n1 = int(raw_input("number 1: "))
        n2 = int(raw_input("number 2: "))
        if n1 < 0 or n2 < 0:
                negmultable(n1, n2)
        else:
                multable(n1, n2)
        again = raw_input("go again?(y/n)")
        if again == "y":
                main()


if __name__ == "__main__":
        main()
