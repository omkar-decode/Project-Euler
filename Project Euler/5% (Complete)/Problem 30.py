n = 1
add = 0
while n<1000000:
    n += 1
    a = [int(i) for i in list(str(n))]
    num = 0
    for j in a:
        num += (j**5)
    if n==num:
        print num
        add += n
print add
