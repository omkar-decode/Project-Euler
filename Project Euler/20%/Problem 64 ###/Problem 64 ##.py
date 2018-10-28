import time
start_time = time.clock()


# the Decimal library is used to achieve arbitrary precision of floating point numbers
from decimal import getcontext, Decimal
getcontext().prec = 100

def SquareRootPeriod (n):
    
    sqrRoot = (n**0.5)
    if (int(sqrRoot) == sqrRoot):
        return 0
    
    mult = 10**20
    
    nums = []
    fracs = []
    root = Decimal(n**0.5)
    a = int(root)
    b = a
    period = 0
    
    while (True):
        if (period != 0):
            nums.append(b)
        
        root = (Decimal(1)/Decimal(root-b))
        b = int(root)
        f = int((root-b)*mult)
        
        if (f in fracs):
            break

        fracs.append(f)
        period += 1

    return period


if __name__ == "__main__":

    n = 10000
    oddPeriod = 0

    for k in xrange(1, n+1):

        period = SquareRootPeriod(k)
        #print k, period
        if (period%2 == 1):
            oddPeriod += 1
            

    print oddPeriod        
    
        
print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec" 

