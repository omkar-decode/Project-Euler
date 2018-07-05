# Calculate the nth Bell's Number using the Bell Triangle

import time

def n_bell(n, upper):

    if n==1:
        return 1

    row = len(upper)

    if row==n:
        return upper[row-1]

    current = [0 for i in xrange(row+1)]
    current[0] = upper[row-1]
    for col in xrange(row):
        current[col+1] = current[col] + upper[col]

    return n_bell(n, current)


print "Enter the value of n:",
num = input()
start_time = time.clock()

print "The " + str(num) + "th Bell Number is " + str(n_bell(num, [1]))

print "Execution time: %.6f sec" % (time.clock() - start_time)
                                        
