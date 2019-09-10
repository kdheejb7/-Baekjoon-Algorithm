from operator import itemgetter 
import sys
peopleCount = int(input())
people = []
for _ in range(peopleCount):
    age, name = sys.stdin.readline().split()
    people.append((int(age),name))
people.sort(key=itemgetter(0))
for i,j in people:
    print(int(i),j)
