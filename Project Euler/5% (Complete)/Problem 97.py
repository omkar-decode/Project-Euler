n = 7830457; big_num = (10**10)
i = 0; power = 0
cond = True
while(cond):
    if (2**i)>n:
        power = (i-1)
        cond = False
    else:
        i += 1

power_nums = []
temp = n
while(temp>0):
    term = (2**power)
    if temp-term>=0:
        power_nums.append(power)
        temp -= term
    power -= 1

power_mods = []
for p in power_nums:
    num = 2
    for i in xrange(1, p+1):
        mod = num%big_num
        num = (mod*mod)%big_num
    power_mods.append(num) 

l = len(power_mods); inter = 1
for q in xrange(l):
    inter = (inter*(power_mods[q]))%big_num
    
final = ((inter*28433)%big_num)+1
print final

