def prime(n):
    if n==2:
        return True
    if n%2==0 or n==1 or n==0:
        return False
    else:
        return all(n%i for i in xrange(3, (n/2)+1, 2))

def trunc_prime(n):
    l = len(str(n))
    return (all(prime(int((str(n))[index:])) for index in xrange(l)) and all(prime(int((str(n))[:(l-index)])) for index in xrange(l)))
   

n = 11; count = 0; add = 0             #takes too much time for generating the last number
while count < 11:
    if prime(n):
        if trunc_prime(n):
            add += n
            count += 1        
    n += 2        

print add
