import time
start_time = time.clock()

# iterate over all the possible coordinates in a manner that a pair of points are not repeated
# check right angle by finding dot product of a pair of sides and comparing with 0

# below function checks if the given two points form a right triangle with the origin    
def IsRightTriangle (x1, y1, x2, y2):
    if (x1==0 and y1==0):
        return False

    if (x2==0 and y2==0):
        return False
    
    if (x1==x2 and y1==y2):
        return False

    expression_one = ((x1*x2) + (y1*y2))
    expression_two = (x1*(x1-x2) + y1*(y1-y2))
    expression_three = (x2*(x1-x2) + y2*(y1-y2))

    if (expression_one==0 or expression_two==0 or expression_three==0):
        return True

    return False


if __name__ == "__main__":

    n = 50
    rightTriangles = 0

    # x2 iterates from 0 to x1 (inclusive) to avoid repitition of pairs of coordinates
    # also, notice that by this method, (x2 <= x1)
    for x1 in xrange(n+1):
        for x2 in xrange(x1+1):
            # y1 iterates from 0 to y2 inclusive since: given that (x2 <= x1), the only way the triangle can be
            # a right triangle is if (y1 <= y2), due to the form of expression_one and expression_two
            for y2 in xrange(n+1):
                for y1 in xrange(y2+1):

                    if (IsRightTriangle(x1, y1, x2, y2)):
                        rightTriangles += 1

    print rightTriangles


print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
