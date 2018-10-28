def prime(n):
    if n%2==0:
        return False
    else:
        for i in xrange(3, (n+1)/2, 2):
            if n%i==0:
                return False
                break
        else:
            return True
        
num = 13
n = 101

while n<1000000:
    for k in list(str(n)):
        if int(k)%2 == 0:
            break
    else:    
        if prime(n):
            a = list(str(n))
            for i in xrange(len(a)-1):
                a.append(a[0])
                a.remove(a[0])
                b = int(''.join(a))
                if not prime(b):
                    break
            else:
                num += 1
    n += 2

print num

