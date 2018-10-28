def palin(n):
    if list(reversed(list(str(n)))) == list(str(n)):
        return True
    else:
        return False

def rev(n):
    return int(''.join(list(reversed(list(str(n))))))

count = 0
for num in xrange(1, 10001):
    i = 1; cond = True; temp = num
    while cond:
        i += 1
        add = temp + rev(temp)
        if palin(add):
            cond = False
        elif i>50:
            count += 1
            cond = False
        else:
            temp = add
            
print count            
             
    
