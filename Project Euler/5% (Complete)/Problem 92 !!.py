#Execution time: 3 to 3.5 min

#find lexicographically shortest form of n
def shorten(n):
    return int("".join(list(sorted(list(str(n))))))

#sum of squares of digits
def num_sqr(n):
    sqr_sum = 0
    while(n!=0):
        sqr_sum += (n%10)*(n%10)
        n /= 10
    return sqr_sum


#check if a number is happy by maintaining two variables
#slow moves 1 step at a time, fast moves 2
def if_happy(n, nums):
    slow = n; fast = n
    nums[n-1] = 1
    while(True):
        
        slow = num_sqr(slow)
        fast = num_sqr(num_sqr(fast))

        nums[slow-1] = 1   
        nums[fast-1] = 1

        if(slow==1 or fast==1):
            return True

        elif(slow==fast):
            return False

#count number of happy numbers in the sequence starting with n
def cnt_happy(n, check, happy_nums):
    count = 0
    num = n
    while(num!=1):
        if(check[num-1]==0):            
            check[num-1] = 1
            count += 1
            ##happy_nums.append(num)

        num = num_sqr(num)

    return count    

#counter for happy numbers
happy = 1

#list of happy numbers
happy_nums = [1]

#nums keeps a track of whether a number has been visited 
nums = [0 for i in xrange(1, 10000000)]

#check keeps a track of whether a number has already been counted as happy
check = [0 for i in xrange(1, 10000000)]

for n in xrange(1, 10000000):
    shorted = shorten(n)
    if(check[n-1]==1):
        continue
    
    elif(check[shorted-1]==1 and n!=shorted):
        nums[n-1] = 1
        check[n-1] = 1
        ##happy_nums.append(n)
        happy += 1
        continue

    if(if_happy(n, nums)):
        happy += cnt_happy(n, check, happy_nums)
   

unhappy = (9999999-happy)
print unhappy
##print list(sorted(happy_nums))
