count = int(input())
location = []
for i in range(count):
    location.append(list(map(int,input().split())))
location.sort()
for i in location:
    print(*i)
