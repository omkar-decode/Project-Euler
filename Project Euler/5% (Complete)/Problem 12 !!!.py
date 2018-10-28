num = 28; count = 0; cond = True
while cond:
        num=num+8+(count)
        count += 1
        n_fac = 1; n = num

        if n%2==0:
            temp = 1
            while n%2==0:
                n /= 2
                temp += 1
            n_fac *= temp    

        for i in xrange(3, int(n**0.5)+1, 2):
            temp = 1
            while n%i==0:
                n=n/i
                temp += 1
            n_fac *= temp

        if n_fac > 500:
            print num
            cond = False

            
            
