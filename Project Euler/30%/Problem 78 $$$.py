# use Dynamic Programming to count number of summations
# idea is similar to 'Coin Change Problem', check at 'https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/'


def countPartitions(n):

    table = [0 for i in xrange(n+1)]

    table[0] = 1
    for i in xrange(1, n):
        for j in xrange(i, n+1):
            table[j] += table[j-i]

    return (1+table[n])
    
   
##print countPartitions(50)
   
currNum = 2
cond = True
mod = 1000000

while(cond):
    numWays = countPartitions(currNum)
    if(numWays%mod == 0):
        cond = False
    else:
        currNum += 1

print currNum        

