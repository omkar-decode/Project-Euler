def fac(n):
    pro = 1
    for i in xrange(2,n+1):
        pro = pro*i
    return pro
s = 0
for n in xrange(3, 9999999):
    sum_dig_fac = sum([fac(int(j)) for j in list(str(n))])
    if n == sum_dig_fac:
        s += n
print s  
                          

