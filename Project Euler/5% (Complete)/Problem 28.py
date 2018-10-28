def f(n):
    return ((4*(n**2)) - (2*n) + 1)             #general term for the elements in the lower right part of the diagonal

count = 0; score = 1
while count < 500:
    count += 1
    score += f(count) + (f(count)+(1*(2*count))) + (f(count)+(2*(2*count))) + (f(count)+(3*(2*count)))

print score
    
