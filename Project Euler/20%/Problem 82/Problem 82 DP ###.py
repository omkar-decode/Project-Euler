import time
start_time = time.clock()

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"


n = 80

f = open("p082_matrix.txt", "r")
grid = f.read().split()

for l in xrange(n):
    grid[l] = map(int, grid[l].split(','))
