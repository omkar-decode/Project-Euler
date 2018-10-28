import time
start_time = time.clock()


def Totient (n):
    phi = n
    p = 2

    while (p * p) <= n:
        
        if n % p == 0:
            while (n % p == 0):
                n /= p

            phi -= (phi / p)

        p += 1    

    if (n > 1):
        phi -= (phi / n)

    return phi

def Expression (n):
    term1 = (15499 * (n-1))
    term2 = (94744 * Totient(n))

    if term1 > term2:
        return True

    return False


if __name__ == "__main__":

    n = 12
    currVal = n

    while (True):
        currVal += 1

        #print currVal
        if (Expression(currVal)):
            break

    print currVal    
    

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
