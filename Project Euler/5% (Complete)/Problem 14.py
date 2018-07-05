n = 999999
num = 0
while n>0:
    m = n
    c = 0
    while m!=1:
        if m%2==0:
            m = m/2
        elif m%2==1:
            m = (3*m)+1
        c += 1
    if c>num:
        num = c
        p = n
    n -= 1
print p
