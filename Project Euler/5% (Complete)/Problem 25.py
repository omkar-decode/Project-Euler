def fib(n):
    a = 1; b = 1
    if n==1:
        return a
    if n==2:
        return b
    if n>2:
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        return b
n = 1
while True:
    if len(str(fib(n)))==1000:
        print n
        break
    n += 1
