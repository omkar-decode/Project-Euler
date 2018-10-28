import time
start_time = time.clock()


def GCD (a, b):
    if (b > a):
        a, b = b, a

    while (a%b != 0):
        c = a%b
        a = b
        b = c

    return b
    
        
def IsEquilateral (a):
    term1 = (((3*a*a) - (2*a) - 1)) ** (0.5)
    term2 = (((3*a*a) + (2*a) - 1)) ** (0.5)

    if (int(term1) == term1):
        if (term1%2 == 0):
            return ((3*a) + 1)

        return False

    if (int(term2) == term2):
        if (term2%2 == 0):
            return ((3*a) - 1)

        return False

    return False



if __name__ == "__main__":


##    n = 100
##    for a in xrange(3, n+1, 2):
##        checkEquilateral = IsEquilateral(a)
##        if (checkEquilateral != False):
##            print checkEquilateral
    limit = (10)*9
    
    sideLimit = (limit // 3)
    check = int((sideLimit)**(0.5))

    numTriangles = 0
    perimeterSum = 0
    
##    m = 1
##    while (m <= check):
##        n = 2
##        hypotenuse = (m*m + n*n)
##        while (hypotenuse <= sideLimit):
##            if (GCD(m, n) != 1):
##                n += 2
##                continue
##
##            checkEquilateral = IsEquilateral(hypotenuse)
##            if (checkEquilateral != False):
##                numTriangles += 1
##                perimeterSum += checkEquilateral
##                
##            n += 2
##
##        m += 2
##
##    print numTriangles
##    print perimeterSum

    
    for a in xrange(3, (sideLimit+1), 2):
        
        checkEquilateral = IsEquilateral(a)
        if (checkEquilateral != False):
            numTriangles += 1
            perimeterSum += checkEquilateral

    print numTriangles
    print perimeterSum        


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"    



        
    
