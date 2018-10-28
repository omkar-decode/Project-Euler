import time
start_time = time.clock()

# the Decimal library is used to achieve arbitrary precision of floating point numbers
from decimal import getcontext, Decimal
getcontext().prec = 102


def DigitalSum (n):
    numString = str(n)

    digitSum = 0
    l = 101
    for d in xrange(l):
        if (numString[d] != "."):
            digitSum += int(numString[d])

    return digitSum


# below is an attempt to find the square root using Binary Search
# however, after a certain number of decimal digits, the value diverges from the correct value

##def FindRoot (l, r, n):
##
##    middle = 1
##    for i in xrange(precision):
##        middle = (Decimal(l)+Decimal(r))/Decimal(2)
##        
##        sqr = Decimal(middle)*Decimal(middle)
##        if (Decimal(sqr) > Decimal(n)):
##            r = Decimal(middle)
##        else:
##            l = Decimal(middle)
##
##    return middle



# the logic of the method below is that for a number n, its square root r satisfies (r == n/r)
# so pick a number p, find q=(n/p), take avg=(p+q)/2, set p=avg and repeat
# here the value converges to the correct value very quickly

def FindRoot (n):

    a = int(n**0.5)

    for i in xrange(precision):
        b = Decimal(n)/Decimal(a)
        a = (Decimal(a) + Decimal(b))/Decimal(2)

    return a    


def SquareRootDigitalSum (n):

    sqrRoot = FindRoot(n)

    return DigitalSum(sqrRoot)

    

if __name__ == "__main__":

    precision = 102
    totalSum = 0
    n = 100

    for x in xrange(1, n+1):
        if (int(x**0.5) == (x**0.5)):
            continue

        totalSum += SquareRootDigitalSum(x)

    print totalSum    



print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
