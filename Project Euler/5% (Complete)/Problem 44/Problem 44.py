import time
start_time = time.clock()


def GetPentagon (n):
    return (n * ((3*n)-1))/2


def IsPentagon (x):
    term1 = ((24*x) + 1) ** (0.5)
    if (int(term1) != term1):
        return False

    if ((term1+1) % 6 == 0):
        return True

    return False


# the approach is a hit and trial one
  
if __name__ == "__main__":

    diffs = []
    limit = 3000
    
    for n in xrange(2, limit):
        for m in xrange(1, n):
            term1 = GetPentagon(n)
            term2 = GetPentagon(m)

            addition = (term1 + term2)
            subtraction = (term1 - term2)

            if (IsPentagon(subtraction) and IsPentagon(addition)) :
                diffs.append([m, n, addition, subtraction])
                


    print diffs           


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
