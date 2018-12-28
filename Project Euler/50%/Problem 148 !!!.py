import time
import math
start_time = time.clock()

# I have used Lucas's Theorem in this problem (https://en.wikipedia.org/wiki/Lucas%27s_theorem)

# Let C(n) represent the number of non-divisible entries in the 'n'th row of Pascal's Triangle
# Notice that C(n) is given by the following expression:
# if a(k-1)a(k-2)...a(1)a(0) is the representation of n in base p (7 in this case), then
#   C(n)  =   [a(k-1)+1]*[a(k-2)+1]*...*[a(1)+1]*[a(0)+1] 

# Let S(n) represent the total number of non-div entries UPTO the first n rows (row number 0 to n-1)
# In the equations below, S(k) has k in base p
# We see that   S(1) = 1        --> first 1 row
#               S(10) = 28      --> first 7 rows
#               S(100) = 28^2   --> first 49 rows

# In general, S(7^m) = 28^m

# For the given problem, we find the base-7 representation of 1,000,000,000 and 
# iterate over the digits from left to right
# In every iteration, we make use of the above formulas for C(n) and S(n)

# the 'multiplier' variable takes care of the contribution of digits 
# to the left of current digit, that we have already considered

# NOTE: the RowNonDivisibles function has not been used in the solution


# takes input n in base-10 and returns the corresponding base-p value of n
def ChangeRadix (n, p):

    e = 1
    d = 0
    while (e <= n):
        e *= p
        d += 1

    exp = d-1
    base_p = 0
    for j in xrange (1, d+1):
        base_p *= 10
        base_p += (n / (p**exp))

        n -= (n / (p**exp))*(p**exp)
        exp -= 1

    return base_p   


# this function returns the number of entries in the 'n'th row of 
# Pascal's Triangle that are NOT divisible by p 
# def RowNonDivisibles (n, p):

#     radix_p = ChangeRadix(n, p)
#     digits = [int(d) for d in str(radix_p)]

#     cnt = 1
#     for d in digits:
#         cnt *= (d+1)

#     return cnt


# this function returns the total number of entries in the first n rows
# of Pascal's Triangle that are NOT divisible by p
def CountNonDivisibles (n, p):

    radix_p = ChangeRadix(n, p)

    digits = [int(d) for d in str(radix_p)]
    num_len = len(digits)

    multiplier = 1
    curr_expo = num_len
    digit_index = 0

    base_sum = sum(range(1, p+1))

    cnt = 0
    while (digit_index < num_len):
        curr_digit = digits[digit_index]
        curr_expo -= 1

        term = (curr_digit*(curr_digit+1))/2
        term *= ((base_sum)**curr_expo)
        term *= multiplier

        cnt += term

        multiplier *= (curr_digit+1)
        digit_index += 1


    return cnt
        

if __name__ == "__main__":

    p = 7
    row_limit = 10**9

    print CountNonDivisibles(row_limit, p)

    print "Execution time: %.5f" %(time.clock() - start_time) + " sec"
