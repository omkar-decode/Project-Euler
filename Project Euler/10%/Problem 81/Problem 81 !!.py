import time
start_time = time.clock()


def minPath(grid):
    n = len(grid)

    for r in xrange(n):
        for c in xrange(n):

            if(r==0 and c==0):
                continue
            
            if(r==0):
                grid[r][c] += grid[r][c-1]

            if(c==0):
                grid[r][c] += grid[r-1][c]

            if(r>0 and c>0):
                grid[r][c] += min(grid[r][c-1], grid[r-1][c])

    return grid[n-1][n-1]            



fp = open("p081_matrix.txt", "r")
grid = fp.read().split('\n')
for l in xrange(80):
    grid[l] = map(int, grid[l].split(','))
grid = grid[:80]


minimal = minPath(grid)
print minimal



print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
