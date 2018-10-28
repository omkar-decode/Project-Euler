import time
start_time = time.clock()

# considering binomial coefficients (nCm), the highest n in this case is 50
# checkout Kummer's Theorem (https://en.wikipedia.org/wiki/Kummer%27s_theorem)
# we see that if a prime p>n, then there is no possible m such that (m + (n-m)) would give a carry, in base p
# hence, we need to check only for primes upto 50

n = 51
pascalTriangle = [[1]]
level = 1

distinct = [1]

# build the Pascal Triangle
for i in xrange(n-1):
    row = [1]
    for j in xrange(1, level):
        elem = (pascalTriangle[i][j-1])+(pascalTriangle[i][j])
        row.append(elem)
        distinct.append(elem)

    row.append(1)    

    pascalTriangle.append(row)
    level += 1    

# print pascalTriangle

distinct = list(set(distinct))
# print len(distinct)

sqrFree = []

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
p = len(primes)

# filter out the square-free numbers
for x in distinct:

    index = 0; flag = 1
    while index<p:
        
        prim = primes[index]
        if (x % (prim * prim) == 0):
            flag = 0
            break
        
        index += 1

    if flag == 1:
        sqrFree.append(x)

print sum(sqrFree)


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
