import time
start_time = time.clock()


def gcd(a, b):
    if a<b:
        temp = a
        a = b
        b = temp

    while b != 0:
        temp = a%b
        a = b
        b = temp

    return a    

max_L = 50
numberTriangles = 0

# a pythagorean triplet is of the form (m^2 - n^2), (2*m*n), (m^2 + n^2)
# perimeter (L) = 2 * m * (m + n)
# so the length of the wire must always be an even integer
# for a given L = 2*k, iterate over m (from 2 to root(k)) and for each m, check if an integer n exists
a = []
for k in xrange(6, ((max_L/2)+1)):

    numberWays = 0
    for m in xrange(2, int(((k)**(0.5))+1)):
        if (k % m != 0):
            continue

        n = ((k/m) - m)
        if (m>n and n >= 1):
            numberWays += 1

            if (numberWays > 1):
                break
            

    if (numberWays == 1):
        numberTriangles += 1
        


print numberTriangles



print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

