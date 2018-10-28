import time
start_time = time.clock()
#print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"

count = 0
octagonal = []
for i in xrange(19, 59):
    num = i*((3*i)-2)
    if((str(num))[2] != '0'):
        print num
        octagonal.append(num)
        count += 1

print count        
