numCount = int(input())
alphabet = []

def quick_sort(mylist):
    if len(mylist) > 1:
        pivot = mylist[-1]
        left, mid, right = [], [], []
        for i in range(len(mylist)-1):
            if len(mylist[i])>len(pivot):
                right.append(mylist[i])
            elif len(mylist[i])<len(pivot):
                left.append(mylist[i])
            else:
                mid.append(mylist[i])
        mid.append(pivot)
        return quick_sort(left)+mid+quick_sort(right)
    else:
        return mylist
    
for i in range(numCount):
    tmp = input()
    if tmp not in alphabet:
        alphabet.append(tmp)
for i in range(len(alphabet)):
    alphabet.sort()
alphabet = quick_sort(alphabet)

print(*alphabet, sep='\n')
