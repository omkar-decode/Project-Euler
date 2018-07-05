import time
start_time = time.clock()



# the idea is to use Inclusion-Exclusion principle to find all possible combinations
# k represents the number of digits in the hexadecimal number
# for k=1 and k=2, number of ways is 0; hence k begins from 3

total = 0

# the terms below were obtained on a pen & paper
for k in xrange(3, 17):

    term1 = (15 * (16**(k-1)))
    term2 = (43 * pow(15, (k-1)))
    term3 = (41 * pow(14, (k-1)))
    term4 = (13 * pow(13, (k-1)))

    total += (term1 - term2 + term3 - term4)
    

# the decimal value of total is converted to hexadecimal
print total

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

















    


