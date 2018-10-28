import time
start_time = time.clock()

  
def IsInsideGrid(x, y):
    if x>=0 and x<n and y>=0 and y<n:
        return True

    return False


# the idea is to apply Dijkstra algorithm to the grid
def ModifiedDijkstra(grid, n, startCell, endCell):

    start_x = startCell[0]
    start_y = startCell[1]

    # initialise the distance array
    dist = [ [INFINITY for i in xrange(n)] for j in xrange(n) ]

    # direction arrays for getting neighbour of a cell
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # format of a node is [x, y, dist]
    visNodes = [[start_x, start_y, 0]]

    # base case
    dist[0][0] = grid[0][0]

    while(len(visNodes) != 0):
        visNodes.sort()
        
        currCell = visNodes[0]
        x = currCell[0]
        y = currCell[1]
        
        visNodes.remove(visNodes[0])

        for i in xrange(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(IsInsideGrid(new_x, new_y) == False):
                continue

            if (dist[new_x][new_y] > dist[x][y] + grid[new_x][new_y]):

                nodeIndex = -1
                
                if ([new_x, new_y, dist[new_x][new_y]] in visNodes):
                    visNodes.remove([new_x, new_y, dist[new_x][new_y]])


                dist[new_x][new_y] = dist[x][y] + grid[new_x][new_y]
                visNodes.append([new_x, new_y, dist[new_x][new_y]])

                

    end_x = endCell[0]
    end_y = endCell[1]
    
    return (dist[end_x][end_y])
                                

if __name__ == "__main__" :

    n = 80
    INFINITY = (10**10)

    f = open("p083_matrix.txt", "r")
    grid = f.read().split()

    for l in xrange(n):
        grid[l] = map(int, grid[l].split(','))

    startCell = [0,0]
    endCell = [n-1, n-1]
    minCost = ModifiedDijkstra(grid, n, startCell, endCell)

    print minCost


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"











        




