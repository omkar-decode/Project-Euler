n = 1; add = 0
while n<=1000:
    add += (n**n)%(10**10)
    add %= (10**10)
    n += 1
  
print add
