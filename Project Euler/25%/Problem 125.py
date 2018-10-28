import time
start_time = time.clock()

# consider all possible consecutive square sums below 10^8 and include the ones which are palindromic

def IsPalindrome (n):
    s = str(n)
    l = len(s)

    for i in xrange(l//2):
        if (s[i] != s[l-i-1]):
            return False

    return True    


if __name__ == "__main__":
    
    limit = 10**8
    numLimit = (limit ** 0.5)

    start = 1
    numPalindromes = 0
    squareSumPalindromes = 0

    nums = []
##    checks = []
    while (start < numLimit):

        squareSum = 0
        currNum = start
        while (squareSum < limit):
            squareSum += (currNum * currNum)

            if (squareSum >= limit):
                break
            
            if (currNum>start and IsPalindrome(squareSum)):
                if (not (squareSum in nums)):
                    
                    numPalindromes += 1
                    squareSumPalindromes += squareSum
                    nums.append(squareSum)
##                    checks.append([start, currNum, squareSum])

            currNum += 1

        start += 1

##    for i in checks:
##        print i
##    print numPalindromes
    print squareSumPalindromes


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec" 
  
