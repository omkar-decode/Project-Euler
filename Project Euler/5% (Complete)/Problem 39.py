sol_max = 0; num = 0
for p in xrange(12, 1001):
    sols = 0
    for x in xrange(1, p/2):
        y = (float(p*((2*x)-p)))/(2*(x-p))
        if int(y)==y and y>x:
            sols+=1
    if sols>sol_max:
        sol_max = sols
        num = p

print sol_max, num       

