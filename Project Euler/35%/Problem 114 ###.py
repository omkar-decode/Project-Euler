import time
start_time = time.clock()
#print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

def factorial(n):
    if(n==0):
        return 1
    return (n * factorial(n-1))

n = 50
num_tiles = [0 for i in xrange(3, 51)]



   
