elem = []
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if c not in elem:
            elem.append(c)
print len(elem)            
