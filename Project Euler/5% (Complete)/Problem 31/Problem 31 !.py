def solutions(elems, m, n):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m<=0 and n>0:
        return 0
    return (solutions(elems, m-1, n) + solutions(elems, m, (n-elems[m-1])))
        
count = 1; n = 200; m = 7
denoms = [1, 2, 5, 10, 20, 50, 100, 200]

count += solutions(denoms, m, n)
print count
                               
