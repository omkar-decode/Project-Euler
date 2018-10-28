import time
start_time = time.clock()

# the approach is to consider n digit numbers, where n starts from 2
# for a given k digit number, the digit sum can vary from k (all digits 1) to 9k (all digits 9)
# for each possible digit sum (say s), find all the powers of s which contain k digits
# for each power of s containing k digits (say p), check if sum of digits of p is s

def SumOfDigits (n):
    s = str(n)
    l = len(s)

    digitSum = 0
    for i in xrange(l):
        digitSum += int(s[i])

    return digitSum


def CheckPower (digitSum, numberOfDigits):
    n = numberOfDigits
    d = digitSum

    if (n == 1):
        return []

    # keep multiplying till we reach a power of digitSum which contains n digits
    while (len(str(d)) < n):
        d *= digitSum

    numbers = []
    while (len(str(d)) == n):
        
        if (SumOfDigits(d) == digitSum):
            numbers.append(d)

        d *= digitSum    

    return numbers


if __name__ == "__main__":
    
    digitPowerNums = []
    n = 2
    termIndex = 30

    while (len(digitPowerNums) < termIndex):
        minSum = n
        maxSum = (9*n)

        for s in xrange(minSum, maxSum):
            digitPowerNums.extend(CheckPower(s, n))

        n += 1    

    print digitPowerNums[termIndex-1]
    

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec" 
