fp = open("pyramid.txt", "r")
lines = fp.read().split('\n')
for l in xrange(100):
    lines[l] = map(int, lines[l].split(' '))

for i in xrange(99):
    nums = lines[i]
    for n in xrange(i+1):
        if n==0:
            lines[i+1][n] += nums[n]
        else:
            greater = max(nums[n], nums[n-1])
            lines[i+1][n] += greater
        if n==i:
            lines[i+1][n+1] += nums[n]    
        
max_sum = max(lines[99])
print max_sum
