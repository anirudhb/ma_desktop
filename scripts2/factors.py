def factors(n):
    sqrt = n//2
    facs = [1, n]
    counter = 0
    for i1 in range(2, sqrt+1):
        if i1 in facs:
            continue
        for i2 in range(i1, sqrt+1):
            if i2 in facs:
                continue
##            counter += 1
##            print counter, i1, i2
            if i1*i2 == n:
                    if i1 not in facs:
                            facs.append(i1)
                    if i2 not in facs:
                            facs.append(i2)
    return sorted(facs)
def factors2(n):
    return set(sum([[i, n//i] for i in range(1, int(n**.5)+1) if not n%i], []))
##def factors2(n):
##    result = [1, n]
##
##    for ix in xrange(2, n):
##        if ix in result:
##            continue
##        if n % ix == 0:
##            result.append(ix)
##            result.append(n/ix)
##
##    return result

import sys
sys.argv.append(65536)
print(factors2(int(sys.argv[1])))
