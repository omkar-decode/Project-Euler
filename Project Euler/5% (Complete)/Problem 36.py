#creating functions for converting decimal to binary

def pow_2(n):                                           #checks if n is a power of 2 
    if n == 1:
        return False
    else:
        temp = n
        while temp%2 ==0:
            temp /= 2
        if temp == 1:
            return True
        else:
            return False

def pow_2_btwn(a, b):                                   #counts number of powers of 2 between a and b both excluded
    c = 0
    for i in xrange(a+1, b):
        if pow_2(i):
            c += 1
    return c                    

def binary(n, num):                                 #converts decimal to binary
    if n==0:
        return num + '0'
    elif n==1:
        return num + '1'
    elif pow_2(n):
        power = 0
        while n%2==0:
            n /= 2
            power += 1
        return num + '1' + (power)*'0'    
    else:
        temp = n; count = 0
        while temp != 1:
            temp /= 2
            count += 1
        num += '1'
        new_val = (n-(2**count))
        n_0 = pow_2_btwn(new_val, n)
        if n_0 >0:
            num += (n_0-1)*'0'
        return binary(new_val, num)


#code related to problem 36

def palin(s):
    if list(reversed(list(str(s)))) == list(str(s)):
        return True
    else:
        return False

add = 0
for num in xrange(1, 1000000):
    if palin(num):
        if palin(binary(num, '')):
            add += num

print add            
                

