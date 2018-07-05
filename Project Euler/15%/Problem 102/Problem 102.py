import time
start_time = time.clock()

def area(x1, y1, x2, y2, x3, y3):
    A = (float(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)))/2
    return abs(A)

fp = open("p102_triangles.txt", "r")
lines = fp.read().strip().split("\n")

# let ABC be the triangle and P be the origin

# the idea is that if the sum of areas of triangles PAB, PBC and PCA equals
# the area of triangle ABC, then P lies inside the triangle

interior = 0
for l in lines:
    coords = map(int, l.split(","))
    x1, y1, x2, y2, x3, y3 = coords

    area_total = area(x1, y1, x2, y2, x3, y3)
    area1 = area(x1, y1, x2, y2, 0, 0)
    area2 = area(x2, y2, x3, y3, 0, 0)
    area3 = area(x3, y3, x1, y1, 0, 0)

    if(area_total == area1 + area2 + area3):
        interior += 1

print interior

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"




