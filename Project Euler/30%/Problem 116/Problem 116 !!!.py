import time
start_time = time.clock()

def nCr(n, r):
    if(n<r):
        return 0
    
    if(r==0):
        return 1

    return ((nCr(n, r-1))*(n+1-r))/r

def num_ways(n, k):
    k -= 1
    i = 1; ways = 0

    while(True):

        if((n-(k*i))<i):
            break

        ways += nCr((n-(k*i)), i)
        i += 1

    return ways

total = 0
for l in xrange(2, 5):
    total += num_ways(50, l)

print total

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


