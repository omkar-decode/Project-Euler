def fib(n):
    import math
    k = (float((5**(0.5))+1))/2
    a = (k*float(n))-(float(1)/n)
    b = (k*float(n))+(float(1)/n)
    if math.ceil(a)<=math.floor(b):
        return True
    else:
        return False
n = 1
s = 0
while n<=4000000:
    if fib(n):
        if n%2==0:
            s += n
    n += 1        
print s            
    

    
    
        

                 



