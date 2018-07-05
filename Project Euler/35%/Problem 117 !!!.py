import time
start_time = time.clock()

def nCr(n, r):
    if(n<r):
        return 0
    
    if(r==0):
        return 1

    return ((nCr(n, r-1))*(n+1-r))/r

def multi_perm(n, x1, x2, x3, x4):
    return (nCr(n, x1))*(nCr((n-x1), x2))*(nCr((n-(x1+x2)), x3))

# the idea is to consider all possible number of tiles of each color, and then reduce all the tiles to tiles of length 1

ways = 0
n = 50
for x in xrange((n/4)+1):
    for y in xrange((n/3)+1):
        for z in xrange((n/2)+1):

            total = n
            if(((4*x)+(3*y)+(2*z))>50):
                continue

            total -= (3*x)
            total -= (2*y)
            total -= (z)

            blank = total - (x+y+z)

            ways += multi_perm(total, x, y, z, blank)

print ways            

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
