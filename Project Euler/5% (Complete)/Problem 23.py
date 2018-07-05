def is_not_sum(n, lis):
    for i in lis:        
        if (n-i)>0 and (n-i) in lis:
            return False
            break
    else:
        return True

def is_abun(n):
    a = 1
    for i in xrange(2,(n/2)+1):
        if n%i==0:
            a += i
    if a>n:
        return True
    else:
        return False

abun_nums = []; add = 0

for i in xrange(12, 28124):
    if is_abun(i):
        abun_nums.append(i)        

for j in xrange(1, 28124):
    if is_not_sum(j, abun_nums):
        add += j

print add        
    



