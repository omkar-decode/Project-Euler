count=0; t=1; a=3; b=2; i=0
while i<1000:
    if len(str(a))>len(str(b)):
        count += 1
    b = a+b
    temp = a
    a = (2*a)+t
    t = temp
    i += 1

print count
