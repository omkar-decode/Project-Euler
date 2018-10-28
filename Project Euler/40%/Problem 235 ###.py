import time
start_time = time.clock()

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


##def binarySearch():




def expression (r):
    # the following are the terms of the simplified summation expression
    term1 = 14100 * (r ** 5001)
    term2 = 14103 * (r ** 5000)
    term3 = 600000000000 * (r * r)
    term4 = 1200000000900 * r
    term5 = 600000000897

    expVal = term1 - term2 - term3 + term4 - term5

    return expVal





if __name__ == "__main__":

    print expression(1)
    print expression(-1.000000000001)

