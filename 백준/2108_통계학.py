import sys
from collections import Counter

def mode(myList):
    mode_dict = Counter(myList)
    modes = mode_dict.most_common()
    if len(myList)>1:
        if modes[0][1]==modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]
    else:
        return modes[0][0]
    
numCount = int(input())
numList = []
for _ in range(numCount):
    numList.append(int(sys.stdin.readline()))
numList.sort()
print(round(sum(numList)/len(numList)))
print(numList[len(numList)//2])
print(mode(numList))
print(max(numList)-min(numList))           #정렬된 후 이므로 numList[-1]-numList[0]해도 된다.
