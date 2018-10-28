import time
start_time = time.clock()


def checkSquareForm(n):
    
    n *= n
    strNum = str(n)
    for i in xrange(1, 10):
        
        if strNum[2*(i-1)] != str(i):
            return False

    return True


if __name__ == "__main__":

    # 3 or 7 will be appended to the number at each iteration
    lowerLimit = 10101010
    upperLimit = 13890266

    root = 0

    for n in xrange(lowerLimit, upperLimit):

        num = int(str(n) + "3")
        if(checkSquareForm(num)):
            root = num
            break

        num = int(str(n) + "7")
        if(checkSquareForm(num)):
            root = num
            break

    root *= 10
    print root



print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


