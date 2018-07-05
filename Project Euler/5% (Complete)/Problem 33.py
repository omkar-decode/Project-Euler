for a in range(11,100):
    for b in range(a+1,100):
        la = [int(i) for i in str(a)]
        lb = [int(i) for i in str(b)]
        for j in la:
            if j in lb:
                if j!=0:
                    la.remove(j)
                    lb.remove(j)
                    if la!=[0] and lb!=[0]:
                        c = (float(lb[0]))/int(la[0])
                        d = float(b)/a
                        if c==d:
                            print str(a)+r'/'+str(b)





