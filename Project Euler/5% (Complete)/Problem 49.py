def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
            break
    else:
        return True
from itertools import permutations
for j in range(1000, 9999):
    if prime(j):
        a = str(j)
        npr = sorted(list(set(list(permutations(a)))))
        for k in npr:
            num = int(''.join(list(k)))
            if num>j and prime(num):
                if prime((2*(num))-j) and ((2*(num))-j)<10000:
                    if sorted(list(str((2*(num))-j)))==sorted(list(str(j))):
                        print j, num, (2*(num))-j
        





