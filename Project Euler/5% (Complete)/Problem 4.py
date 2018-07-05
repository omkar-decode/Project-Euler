def pal(n):
    l = list(str(n))
    a = []
    for i in range(len(l)-1, -1, -1):
        a.append(l[i])
    if a==l:
        return True
    else:
        return False
num = 1
for i in range(100, 1000):
    for j in range(i, 1000):
        if pal(i*j):
            if (i*j)>num:
                num = i*j
print num            
  
    
    
    
        

                 



