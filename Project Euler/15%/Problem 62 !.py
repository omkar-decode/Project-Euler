import time
start_time = time.clock()

# the approach is to simply find the lexicographically smallest permutation
# of a given cube (say p) and increment the frequency corresponding to p

def LeastPerm (n):

    s = list(str(n))
    s.sort()

    return "".join(s)


if __name__ == "__main__":

    cubeFreq = {}
    n = 345
    perms = 5
    
    while (True):

        cube = (n*n*n)
        least = LeastPerm(cube)

        if (not(least in cubeFreq)):
            cubeFreq[least] = [1, cube]
        else:
            cubeFreq[least][0] += 1
            

        if (cubeFreq[least][0] == perms):
            minCube = cubeFreq[least][1]
            break

        n += 1
        

    print minCube        


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec" 
