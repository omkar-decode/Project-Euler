from itertools import permutations

def is_prime(num):
    if num%2 == 0:
        return False
    else:
        return all(num % i for i in xrange(3, (int(num**(0.5)) + 1), 2))

cond = True; n = '987654321'
while cond:
    str_perms = [list(i) for i in list(permutations(n))] 
    perms = sorted([int(''.join(j)) for j in str_perms])
    perms.reverse()

    for p in perms:
        if is_prime(p):
            print p
            cond = False
            break
    else:
        new_str = n[1:]
        n = new_str

    
    
    
