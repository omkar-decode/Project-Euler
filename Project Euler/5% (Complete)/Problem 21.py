def sum_div(n):
    add = 0
    for i in range(1,(n/2)+1):
        if n%i==0:
            add += i
    return add
k = 0
num = 0
while k<10000:
    k += 1
    if sum_div(sum_div(k))==k:
        if k<sum_div(k):
            num += (k+sum_div(k))
print num        
        
