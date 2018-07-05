import time
start_time = time.clock()

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


def dioph(a, n):

    l = len(a)
    if(l==1):
        if(n%(a[0])==0):
            return 1
        return 0

    remain = [dioph(a[1:], n-(k*a[0])) for k in xrange((n/a[0])+1)]
    return sum(remain)

print dioph([2,3,4], 5)

