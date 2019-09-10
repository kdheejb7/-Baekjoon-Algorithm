numCount = int(input())
number = []
for i in range(numCount):
    number.append(int(input()))
number.sort()
print(*number, sep='\n')
