def period(num):
    a = True; i = 0
    while a:
        i += 1
        if (10**i) % num == 1:
            a = False
            return i

max_period = 0        
for j in xrange(3, 1000):
    if j%2==0 or j%5==0:
        continue
    else:
        per = period(j)
        if per > max_period:
            max_period = per
        
print (max_period+1)    
