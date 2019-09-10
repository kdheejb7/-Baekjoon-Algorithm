import sys
count, stand = map(int,input().split())
w = list(map(int,input().split()))
for i in range(len(w)):
    if w[i] < stand:
        print(w[i],end=" ")
