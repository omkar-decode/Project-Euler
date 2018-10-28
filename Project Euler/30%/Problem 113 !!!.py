import time
start_time = time.clock()

def nCr(n, r):
    if(r==1):
        return n

    return ((nCr(n, r-1))*(n+1-r))/r

# the main idea is that the number of non-decreasing sequences of m digits can be found using
# (n1 ones, n2 twos,..., n9 nines) --> (n1 + n2 + ... + n9) = m, where 0 <= n(i) <= m
# same for number of non-increasing sequences

# non-decreasing can be found directly since a k digit number can be written as (100-k) zeros followed by the number
increasing = (nCr(109, 9)) - 1
decreasing = 0

for digits in xrange(2, 101):
    decreasing += (nCr(digits+9, 9))
    decreasing -= 10

non_bouncy = increasing + decreasing
print non_bouncy

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
