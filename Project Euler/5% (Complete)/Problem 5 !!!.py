def prime(n):
    for i in xrange(2, n):
        if n%i == 0:
            return False
            break
    else:
        return True

def pr_less(n):
    prime_nos = []
    for i in xrange(2, n+1):
        if prime(i):
            prime_nos.append(i)
    return prime_nos

##print 'Enter space separated integers:\n',
nos = map(int, [i for i in xrange(1, 21)])
nums = [p for p in nos if p >= 1]
lcm_facts = []
lar = max(nums)
p_facts = pr_less(lar)

for i in p_facts:
    n = 0
    for j in nums:
        tot = 0
        while j%i == 0 and j>=i:
            tot += 1
            j /= i
        if tot>n:
            n = tot
    a = (i**n)
    lcm_facts.append(a)

lcm = 1
for k in lcm_facts:
    lcm *= k
print 'LCM =', lcm

