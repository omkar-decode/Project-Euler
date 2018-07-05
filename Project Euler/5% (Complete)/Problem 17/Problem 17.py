import inflect
p = inflect.engine()

count = 0
for i in xrange(1, 1001):
    word = p.number_to_words(i)
    for j in list(word):
        if j.isalpha():
            count += 1

print count            
