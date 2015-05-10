#!/usr/bin/env python
# Improper Fraction To Mixed Number

def if2mn(n1, n2):
	wh = str(n1/n2)
	fr = str(n1%n2) + "/" + str(n2)
	if fr[0] == "0":
		return wh
	if wh == "0":
                return fr
	return wh + " " + fr

n1, n2 = (int(i) for i in raw_input("Fraction: ").split("/"))
print if2mn(n1, n2)