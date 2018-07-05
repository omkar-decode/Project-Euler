a = [' ']
n = 1
while n<=1000000:
    a.extend(list(str(n)))
    n += 1
print int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000])*int(a[1000000])
