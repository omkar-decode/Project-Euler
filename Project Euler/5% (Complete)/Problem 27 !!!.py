def prime(n):
    if n>0:
        return all(n % i for i in xrange(3, (int(n**(0.5)) + 1), 2))
    else:
        return False

max_prime = 0;
for a in xrange(-999, 1000, 2):
    for b in xrange(1, 1000, 2):
        n = 0; cond = True
        while cond:
            if prime((n**2)+(a*n)+b):
                n += 1
            else:
                cond = False
                if n > max_prime:
                    max_prime = n
                    coeff_a = a
                    coeff_b = b

print coeff_a, coeff_b



#The catch is that all the prime numbers generated must be positive. Hence b>0
