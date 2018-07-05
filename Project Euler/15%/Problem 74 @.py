import time
start_time = time.clock()


def factorial(n):
    if(n==0 or n==1):
        return 1

    fact = 1
    for i in xrange(2, n+1):
        fact *= i

    return fact    

def digit_fact(n):
    total = 0
    digits = map(int, list(str(n)))
    for d in digits:
        total += factorial(d)

    return total    


count = 0
nums = [-1 for i in xrange(1000001)]
nums[1] = 1; nums[2] = 1
storage = []; chain_len = 0

for n in xrange(3, 1000000):
    if(nums[n] != (-1)):
        continue

    storage = [n]
    chain_len = 1
    
    s = digit_fact(n)
    while not s in storage:
        storage.append(s)
        chain_len += 1 

        s = digit_fact(s)

    if(chain_len==60):
        count += 1
        nums[n] = 60
        for j in storage[1:]:
            if(j<1000000):
                nums[j] = 1

    else:
        for j in storage:
            if(j<1000000):
                nums[j] = 1

print count   
            
print "Execution time: %.4f" %(time.clock() - start_time) + " sec"    
