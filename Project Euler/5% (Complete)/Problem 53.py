def fac(n):
    prod = 1
    for i in xrange(2, n+1):
        prod *= i
    return prod

def nCr(n, r):
    return fac(n)/((fac(n-r)*fac(r)))

count = 0
for n in xrange(23, 101):
    for r in xrange(4, n-3):
        if nCr(n, r) > 1000000:
            count += 1

print count
