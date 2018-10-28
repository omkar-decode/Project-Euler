import time
start_time = time.clock()

#the main idea is that the number of rectangles in an n*m grid is ((n+1)C2)*((m+1)C2)

limit = 8000000
min_diff = 1000
closest = [0, 0]

for m in xrange(2, 2001):
    k = (float(limit))/(m*(m-1))
    n = int(0.5 + ((k+0.25)**(0.5)))

    for i in xrange(n-1, n+1):
        diff = abs((i*(i+1)*m*(m+1))-limit)
        if(diff<min_diff):
            closest[0] = m
            closest[1] = i
            min_diff = diff

print "Dimenstions are %d, %d" %(closest[0], closest[1])
print "Area is " + str(closest[0]*closest[1])

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
