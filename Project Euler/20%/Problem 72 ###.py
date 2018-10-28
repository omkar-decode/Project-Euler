import time
start_time = time.clock()

##def next_frac(num, denom, N):
##    a = num[0]; b = denom[0]
##    c = num[1]; d = denom[1]
##
##    k = (N+b)/d
##    new = [((k*c)-a), ((k*d)-b)]
##
##    return new
##
##N = 7
##num = [0, 1]
##denom = [1, N]
##
##count = 1
##cond = True
##
##while(cond):
##
##    nxt = next_frac(num, denom, N)
##    if(nxt == [1, 1]):
##        cond = False
##        break
##    
##    num[0] = num[1]
##    denom[0] = denom[1]
##
##    num[1] = nxt[0]
##    denom[1] = nxt[1]
##
##    count += 1
##
##print count

def next_frac(b, d, N):
    
    k = (N+b)/d
    next_denom = (k*d)-b

    return next_denom

#N = 1000000
N = 10
b = 1; d = N

count = 1
cond = True

while(cond):

    denom = next_frac(b, d, N)
    if(denom == 2):
        cond = False
        break
    
    b = d
    d = denom

    count += 1

print (2*count)+1


print "Execution time: %.4f" %(time.clock() - start_time) + " sec"
