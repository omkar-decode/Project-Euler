import time
start_time = time.clock()

def hcf(a, b):
    dividend = max(a, b); divisor = min(a, b); rem=1
    while True:
        quotient = dividend/divisor
        rem = dividend%divisor
        if rem==0:            
            return divisor
            break
        dividend = divisor
        divisor = rem  

def frac_sum(fracs):
    a1, b1, a2, b2 = fracs
    numer = (a1*b2)+(a2*b1)
    denom = (b1*b2)
    gcd = hcf(numer, denom)
    numer /= gcd
    denom /= gcd
    return '%s/%s' %(numer, denom)

nums = []
for i in xrange(1, 34):
    nums.extend([1, (2*i), 1])    
    

nu=1; de=1  
for j in xrange(97, -1, -1):
    s = frac_sum([nums[j], 1, int(de), int(nu)])
    nu, de = map(int, s.split('/'))

a = map(int, frac_sum([2, 1, de, nu]).split('/'))
print sum(map(int, list(str(a[0]))))

print "Execution time: %.4f" %(time.clock() - start_time) + " sec"

