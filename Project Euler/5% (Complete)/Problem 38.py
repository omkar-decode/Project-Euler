def pand_9(n):
    s = list(str(n))
    if not '0' in s:
        if len(set(s))==len(s):
            return True
        else:
            return False
    else:
        return False

pand_max = 0
for num in xrange(26, 34):
    i = 0; val = ''
    while i<4:
        i +=1
        val += str(i*num)
    if pand_9(val):
        if val > pand_max:
            pand_max = val

for num in xrange(100, 1000):
    i = 0; val = ''
    while i<3:
        i +=1
        val += str(i*num)
    if pand_9(val):
        if val > pand_max:
            pand_max = val            

for num in xrange(9000, 10000):
    i = 0; val = ''
    while i<2:
        i +=1
        val += str(i*num)
    if pand_9(val):
        if val > pand_max:
            pand_max = val 

print pand_max
