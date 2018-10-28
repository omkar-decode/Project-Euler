def is_prime(num):                                                                       
    return all(num % i for i in xrange(3, (int(num**(0.5)) + 1), 2))            #checks if num is prime

add = 2
for j in xrange(3, 2000000, 2):
    if is_prime(j):
        add += j

print add

    
    
        

                 



