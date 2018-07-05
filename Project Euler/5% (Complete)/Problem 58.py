def prime(num):
    if num==3 or num==5:
        return True
    else:
        return all(num % i for i in xrange(3, (int(num**(0.5)) + 1), 2))

def f(n):
    return ((4*(n**2)) - (2*n) + 1)

count = 0; cond = True; store = 0
while cond:
    n_prime = store; count += 1
    if prime(f(count)):
        n_prime += 1
    if prime(f(count)+(1*(2*count))):
        n_prime += 1
    if prime(f(count)+(2*(2*count))):
        n_prime += 1

    store = n_prime
    ratio = float(n_prime)/((4*count)+1)
    if ratio < 0.1:
        print (2*count)+1
        cond = False

 
