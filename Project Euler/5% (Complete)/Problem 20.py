def fact(n):
    pro = 1
    for i in range(2,n+1):
        pro = pro*i
    return pro
a = str(fact(100))
add = 0
for j in a:
    add += int(j)
print add    
