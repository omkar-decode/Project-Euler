import time
start_time = time.clock()


bouncy = 19602
non_bouncy = 2178
n = 21781
cond = True
while(cond):

    if(((bouncy+non_bouncy)*99) == (bouncy*100)):
        cond = False
        break

    #simply check if the number is increasing or decreasing    
    num = list(str(n))
    if(list(sorted(num)) == num):
        non_bouncy += 1

    else:
        if(list(sorted(num, reverse=True)) == num):
            non_bouncy += 1
        else:    
            bouncy += 1

    n += 1        
        

print (bouncy+non_bouncy)       

print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
  
    
