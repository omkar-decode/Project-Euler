n = 40755; cond = True; count = 0
while cond:
    n = (n+573+(count*4))
    exp_1 = (1+(8*n))**0.5
    exp_2 = (1+(24*n))**0.5
    if all([exp_1==int(exp_1), exp_2==int(exp_2), (1+exp_1)%4==0, (1+exp_2)%6==0]):
        print n
        cond = False
    count += 1
