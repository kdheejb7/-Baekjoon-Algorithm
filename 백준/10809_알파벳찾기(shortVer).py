import string
word = input()
for i in string.ascii_lowercase:
    print(word.find(i), end=' ')
