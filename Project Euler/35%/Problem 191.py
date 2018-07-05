import time
start_time = time.clock()           

# below is a mathematical solution to the problem
# problem can be solved using DP as well

numDays = 30

# ConsecThreeA(n) returns the number of strings of length n which have 3 consecutive 'A's
# the method has O(n) complexity, which is fine since n=30
def ConsecThreeA(n):

    if(n<=2):
        return 0
    if(n==3):
        return 1

    # the recurrence relation is: a(n) = 2*a(n-1) + 2*a(n-2) + 2*a(n-3) + 3^(n-3)
    a1 = 0
    a2 = 0
    a3 = 1

    for i in xrange(4, (n+1)):
        a_next = (2 * (a3 + a2 + a1)) + (3 ** (i-3))

        a1 = a2
        a2 = a3
        a3 = a_next

    return a3


# atLeastTwoL(n) returns the number of strings of length n having at least 2 'L's
def AtLeastTwoL(n):

    numStrings = (3 ** n) - ((n+2) * (2 ** (n-1)))

    return numStrings


# following two are helper functions for calculating the set_intersection of above two
#___________________________________________________________________________________________________________________________________________________________________

# ConsecThreeA_and_NoL(n) returns the number of strings of length n having three consecutive 'A's and no 'L's
def ConsecThreeA_and_NoL(n):

    if(n<=2):
        return 0
    if(n==3):
        return 1

    # the recurrence relation is: a(n) = a(n-1) + a(n-2) + a(n-2) + 2^(n-3)
    a1 = 0
    a2 = 0
    a3 = 1

    for i in xrange(4, (n+1)):
        a_next = (a3 + a2 + a1 + (2 ** (i-3)))

        a1 = a2
        a2 = a3
        a3 = a_next

    return a3


# ConsecThreeA_and_OneL(n) returns the number of strings of length n having three consecutive 'A's and exactly one 'L'
def ConsecThreeA_and_OneL(n):

    # 'L' is placed at (k+1)th index, partitioning the string into two strings of length (k) and (n-k-1)
    numStrings = 0

    for k in xrange(n):

        # totalStrings stores number of strings possible for the two partitions ( which is 2^(k) * 2^(n-k-1) )
        totalStrings = (2 ** (n-1))

        # noConsecA stores number of string combinations such that neither left nor right side of 'L' contains three consecutive 'A's
        noConsecA = ((2 ** k) - ConsecThreeA_and_NoL(k)) * ((2 ** (n-1-k)) - ConsecThreeA_and_NoL(n-1-k))

        # numStrings stores number of strings which have three consecutive 'A's on at least one side of the partition
        numStrings += (totalStrings - noConsecA)

    return numStrings    
        

#___________________________________________________________________________________________________________________________________________________________________


    
    


if __name__ == "__main__":

    n = numDays

    # term1 stores number of strings of length n having three consecutive 'A's
    term1 = ConsecThreeA(n)

    # term2 stores number of strings of length n having at least two 'L's
    term2 = AtLeastTwoL(n)
    
    # term3 stores number of strings of length n having three consecutive 'A's AND at least two 'L's
    term3 = (term1 - (ConsecThreeA_and_NoL(n) + ConsecThreeA_and_OneL(n)))


    # totalStrings stores the required answer, calculated by using set_union properties
    totalStrings = (3 ** n) - ((term1 + term2) - term3)

    print totalStrings


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

             























