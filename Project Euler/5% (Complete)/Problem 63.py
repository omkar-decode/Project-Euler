import math

cond = True; count = 0; i = 0
while cond:
    low_lim = int(math.ceil(10**(float(i)/(i+1))))
    if low_lim == 10:
        cond = False
        print count
    else:
        count += (10 - low_lim)
    i += 1
        
