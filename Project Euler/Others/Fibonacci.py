import math

def fib_index(F):
    a = math.log((F*((5)**(0.5)))+0.5)
    b = math.log(((5**0.5)+1)/2)
    return int(math.floor(a/b))

for i in xrange(1, 40):
    print i, fib_index(i)
               
