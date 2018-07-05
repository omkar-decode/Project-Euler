f = open('names.txt')

for w in f:
    word_list = w.split(',')
    break

sorted_list = sorted(word_list)

score = 0
for c, word in enumerate(sorted_list):
    i = c+1
    for letter in list(word[1:len(word)-1]):
        val = i*(ord(letter)-64)
        score += val

print score        
        



