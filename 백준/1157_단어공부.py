from collections import Counter
word = input().upper()
dict_word = Counter(word)
dict_word = dict_word.most_common()

if len(dict_word) != 1 and dict_word[0][1] == dict_word[1][1]:
    print('?')
else:
    print(dict_word[0][0])
    
