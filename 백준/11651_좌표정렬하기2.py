count = int(input())
location = []
for i in range(count):
    tmp = list(map(int,input().split()))
    tmp = tmp[::-1]
    location.append(tmp)
location.sort()
for i in location:
    i.reverse()
    print(*i)
