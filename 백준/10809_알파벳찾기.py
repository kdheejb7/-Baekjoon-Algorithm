import string
word = {}
word_list = list(input())
for index,value in enumerate(word_list) :
    if value not in word:
        word[value] = index

for i in string.ascii_lowercase:
    if i in word:
        print(word[i],end=' ')
    else:
        print(-1, end=' ')
