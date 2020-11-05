review = []
count = 0
with open('IO_file-reviews_analytics.txt', 'r') as f1:
    for line in f1:
        review.append(line)
        count += 1
        if count % 100000 == 0:
            print (len(review))

words_count = {}
for i in review:
    words = i.split(" ")
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
            #新增新的key在wc字典裡

for word in words_count:
    if words_count[word] > 1000000:
        print (word, words_count[word])

print (len(words_count))

while True:
    word = input('which character u wanna search: ')
    if word == 'q':
        break
    elif word in words_count:
        print (word, '出現過', words_count[word], '次。')
    else:
        print ('沒出現過餒')