# use Dynamic Programming to count number of summations
# idea is similar to 'Coin Change Problem', check at 'https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/'

import time
start_time = time.clock()


def countPartitions(n):

    table = [0 for i in xrange(n+1)]

    table[0] = 1
    for i in xrange(1, n):
        for j in xrange(i, n+1):
            table[j] += table[j-i]

    #print table
    return table[n]


#n = int(raw_input())
n = 100
ways = countPartitions(n)
print ways

print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
