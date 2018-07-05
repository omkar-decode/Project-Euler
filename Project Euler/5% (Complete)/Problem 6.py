def sum_sqr(n):
    add = 0
    for i in range(1, n+1):
        add += i
    return (add)**2
def sqr_sum(n):
    add = 0
    for i in range(1, n+1):
        add += (i**2)
    return add
print sum_sqr(100)-sqr_sum(100)
