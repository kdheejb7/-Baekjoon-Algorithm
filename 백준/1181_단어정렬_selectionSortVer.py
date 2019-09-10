numCount = int(input())
alphabet = []
    
for i in range(numCount):
    tmp = input()
    if tmp not in alphabet:
        alphabet.append(tmp)
for i in range(len(alphabet)):
    alphabet.sort()


for i in range(0,len(alphabet)-1):
    for j in range(i+1,len(alphabet)):
        if(len(alphabet[i])>len(alphabet[j])):
            temp = alphabet[i]
            alphabet[i] = alphabet[j]
            alphabet[j] = temp


print(*alphabet, sep='\n')
