import time
start_time = time.clock()

# max_rem() is a function which finds the maximum possible remainder when 'a' is divided by any multiple of 'k'
def max_rem(a, k):
    rems = []; n = 1
    rem = (k*n)%a
    while(rem != 0):
        n += 1
        rems.append(rem)
        rem = (k*n)%a

    return max(rems)

# the main idea is that if n is even, the remainder is always 2, and if n is odd, the remainder is always (2an)
rem_sum = 0
for a in xrange(3, 1001):
    rem_sum += max_rem((a*a), (2*a))

print rem_sum

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

        
    
