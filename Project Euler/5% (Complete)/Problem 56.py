def digit_sum(n):
    digits = map(int, list(str(n)))
    return sum(digits)

dig_max = 0
for a in xrange(3, 100):
    if a%10 == 0:
        continue
    for b in xrange(3, 100):
        add = digit_sum(a**b)
        if add>dig_max:
            dig_max = add
            
print dig_max
