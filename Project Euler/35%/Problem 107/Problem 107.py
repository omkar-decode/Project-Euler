import heapq
import time
start_time = time.clock()


fp = open("p107_network.txt", "r")
lines = fp.read().split('\n')
for l in xrange(40):
    lines[l] = lines[l].split(',')

# use Prim's algorithm to find the MST weight sum

# following prims function returns the sum of weights of MST
def prims(visited, adjMatrix, start):

    nodes = [[0, start]]
    heapq.heapify(nodes)
    minWeightSum = 0
    
    
    while len(nodes)!=0:
        currNode = heapq.heappop(nodes)
        curr = currNode[1]
        if visited[curr] == True:
            continue

        minWeightSum += currNode[0]
        visited[curr] = True

        for i in xrange(n):
            if(adjMatrix[curr][i] == '-'):
                continue
            
            nextNode = i
            if visited[nextNode] == False:
                weight = int(adjMatrix[curr][nextNode])
                heapq.heappush(nodes, [weight, nextNode])
       

    return minWeightSum



if __name__=="__main__":

    n = 40
    visited = [False for i in xrange(n)]
    adjMatrix = lines
    start = 0

    initialWeightSum = 0;
    for i in xrange(n):
        for j in xrange(n):
            
            if(adjMatrix[i][j] != '-'):
                initialWeightSum += int(adjMatrix[i][j])
                
    # divide by two since the adjacency matrix is symmetric
    initialWeightSum /= 2            
        
    minWeightSum = prims(visited, adjMatrix, start)

    print (initialWeightSum - minWeightSum)


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"    
