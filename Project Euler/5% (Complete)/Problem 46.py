def is_sqr(n):
    if int(n**(0.5))== n**(0.5):
        return True
    else:
        return False

def prime(n):
    for i in xrange(3, n, 2):
        if n%i == 0:
            return False
            break
    else:
        return True

def less_prime(n):
    pr_nos = []
    for i in xrange(3, n-1, 2):
        if prime(i):
            pr_nos.append(i)
    return pr_nos


cond = True; num = 7
while cond:
    num += 2
    if not prime(num):
        for j in less_prime(num):
            if is_sqr((num-j)/2):
                break
        else:
            cond = False
print num
    
