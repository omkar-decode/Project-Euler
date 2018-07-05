import time
start_time = time.clock()

def pandigital(n):
    num = list(sorted(set(n)))

    if(len(num)<9):
        return False

    if(num[0] == '1'):
        return True

    return False

a = 1; b = 1; count = 2
while(True):
    count += 1
    c = a + b

    s = str(c)
    l = len(s)

    if(l<575):
        a = b
        b = c
        continue

    first_nine = s[:9]
    if(pandigital(first_nine)):

        last_nine = s[(l-9):]
        if(pandigital(last_nine)):
            print count
            break

    if(count%10000 == 0):
        print count

    a = b
    b = c

print ("Execution time: %.4f" %(time.clock() - start_time)) + " sec"
