import math

fp = open("numbers.txt", "r")
lines = fp.read().split("\n")
max_log = 0.0; count = 0; pair = []; line_num = 0
for line in lines:
    line_num += 1
    base, expo = map(int, line.split(','))
    log = expo*(math.log(base, 10))
    if log>max_log:
        max_log = log
        pair = [line, line_num]

print pair

#max valued number would have max valued logarithm
