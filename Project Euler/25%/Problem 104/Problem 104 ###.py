# check out the website:
#http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibmaths.html#section1.1

import time
start_time = time.clock()

# the code below takes an excessive amount of time to execute and produce output

##def CheckPandigital (n):
##    numString = str(n)
##    d = len(numString)
##    firstNine = map(int, list(set(numString[:9])))
##    lastNine = map(int, list(set(numString[(d-9):])))
##    
##    if (sum(firstNine)==45 and sum(lastNine)==45):
##        return True
##
##    return False
##    
##
##def MatrixMultiply (F, M):
##    x =  F[0][0]*M[0][0] + F[0][1]*M[1][0]
##    y =  F[0][0]*M[0][1] + F[0][1]*M[1][1]
##    z =  F[1][0]*M[0][0] + F[1][1]*M[1][0]
##    w =  F[1][0]*M[0][1] + F[1][1]*M[1][1] 
##
##    F[0][0] = x
##    F[0][1] = y
##    F[1][0] = z
##    F[1][1] = w
##
##
##def MatrixPower (F, n):
##    if (n==0 or n==1):
##        return
##
##    M = [[1,1], [1,0]]
##
##    MatrixPower(F, n/2)
##    MatrixMultiply(F, F)
##
##    if (n%2 == 1):
##        MatrixMultiply(F, M)
##
##
##def Fibonacci (n):
##    F = [[1,1], [1,0]]
##    if (n == 0):
##        return 0
##
##    MatrixPower(F, n-1)
##    return F[0][0]
##
##
##if __name__ == "__main__":
##
##    n = 2749
##    currentNum = n
##    k = -1
##    while (currentNum < ):
##        currentNum += 1
##
##        if (CheckPandigital(Fibonacci(currentNum))):
##            k = currentNum
##            break
##
##    print k



print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
