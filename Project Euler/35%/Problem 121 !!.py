import time
start_time = time.clock()

# the idea is to consider every permutation where (blue > red) and find total number of such cases

# below function returns the next lexicographically higher string 
def NextHighestWord (string):
    s = [ord(i) for i in string]
    
    # find non-increasing suffix from last
    i = (len(s) - 1)
    while i > 0 and s[i-1] >= s[i]:
        i -= 1
        
    if i <= 0:
        return False

    # next element to highest is pivot
    j = len(s) - 1
    while s[j] <= s[i -1]:
        j = j - 1
    s[i-1], s[j] = s[j], s[i-1]

    # reverse the suffix
    s[i:] = s[(len(s)-1) : (i-1) : -1]
    ans = [chr(i) for i in s]
    ans = ("".join(ans))

    return ans


# below function counts the number of wins for a given sequence of blue(B) and red(R) disks
# to find the numerator of the probability of a win, we use the following logic:
# at the (k)th draw, numerator(probability of blue)==1 and numerator(probability of red)==k
# numerator(probability of win) == product of the n numerators obtained by above logic
# probability of win == (numerator / (n!))
def NumberOfWins (blue, red):

    n = (blue + red)
    discOrder = ((blue * "B") + (red * "R"))

    wins = 0
    while (discOrder != False):
        product = 1
        for c in xrange(n):
            if (discOrder[c] == 'R'):
                product *= (c+1)

        wins += product
        discOrder = NextHighestWord(discOrder)

    return wins


if __name__ == "__main__":

    n = 15

    blue = (n/2)+1
    totalWins = 0
    for b in xrange(blue, n+1):
        r = (n - b)
        totalWins += NumberOfWins(b, r)


    totalCases = 1
    for i in xrange(2, n+2):
        totalCases *= i

    maxFund = (totalCases // totalWins)
    #print totalWins, totalCases

    print maxFund


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"    
        
    
