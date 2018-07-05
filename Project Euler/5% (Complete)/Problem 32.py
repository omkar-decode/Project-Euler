nums = []
req = ['1','2','3','4','5','6','7','8','9']
for a in range(11,100):
    for b in range(111,1000):
        x = list(str(a*b))
        x.extend(list(str(a)))
        x.extend(list(str(b)))
        if sorted(x)==req:
            if a*b not in nums:
                nums.append(a*b)

for a in range(1,10):
    for b in range(1111,10000):
        x = list(str(a*b))
        x.extend(list(str(a)))
        x.extend(list(str(b)))
        if sorted(x)==req:
            if a*b not in nums:
                nums.append(a*b)
        
print sum(nums)
        


