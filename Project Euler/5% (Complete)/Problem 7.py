def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    else:
        return True
counter = 1
a = 1
k = int(raw_input())
while counter<k:
    a += 2
    if is_prime(a):
        counter += 1
print a    
    
    
    
        

                 



