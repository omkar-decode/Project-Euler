import time
start_time = time.clock()

frac_right = [3, 7]
frac_left = [2, 5]
num = frac_left[0]
denom = frac_left[1]
condition = True

#the idea behind the operation is the properties of a Farey Sequence; if a/b and c/d are consecutive in F(n),
#then the fraction in between them with the smallest denominator would be (a+c)/(b+d)
while(condition):
    num = frac_left[0]
    denom = frac_left[1]
    
    frac_left[0] += frac_right[0]
    frac_left[1] += frac_right[1]

    #(a+b)/(c+d) will ALWAYS generate a reduced fraction

    #check if the denominator has exceeded the limit
    if(frac_left[1] > 1000000):
        break

       
print num, denom    

print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
