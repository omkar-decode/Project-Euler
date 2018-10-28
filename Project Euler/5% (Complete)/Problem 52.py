n = 0
while True:
    n+=1
    if sorted(list(str(2*n)))==sorted(list(str(3*n)))==sorted(list(str(4*n)))==sorted(list(str(5*n)))==sorted(list(str(6*n))):
        print n
        break
    
