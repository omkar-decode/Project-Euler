##import time
##start_time = time.clock()
##
##
##max_L = 50
##numberTriangles = 0
##
### a pythagorean triplet is of the form (m^2 - n^2), (2*m*n), (m^2 + n^2)
### perimeter (L) = 2 * m * (m + n)
### so the length of the wire must always be an even integer
### for a given L = 2*k, iterate over m (from 2 to root(k)) and for each m, check if an integer n exists
##a = []
##for k in xrange(6, ((max_L/2)+1)):
##
##    numberWays = 0
##    for m in xrange(2, int(((k)**(0.5))+1)):
##        if (k % m != 0):
##            continue
##
##        n = ((k/m) - m)
##        if (m>n and n >= 1):
##            numberWays += 1
##
##            if (numberWays > 1):
##                break
##            
##            a.append([m, n])
##
##    if (numberWays == 1):
##        numberTriangles += 1
##        
##
##
##print numberTriangles
##print a
##
##
##print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
for i in xrange(1, 10):
    for j in xrange(1, i):

        print (i**2 - j**2), (2*i*j), (i**2 + j**2)
