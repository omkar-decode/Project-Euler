from itertools import permutations
a = '0123456789'
print ''.join((sorted(list(permutations(a))))[999999])
