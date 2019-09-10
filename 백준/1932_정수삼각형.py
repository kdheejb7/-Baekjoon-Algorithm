lineCount = int(input())
list2 = [list(map(int, input().split())) for _ in range(lineCount)]
for i in range(1,lineCount):
    list2[i][0] = list2[i-1][0] + list2[i][0]
    list2[i][i] = list2[i-1][i-1] + list2[i][i]
    for j in range(1,i):
        list2[i][j] = max(list2[i-1][j-1], list2[i-1][j]) + list2[i][j]

print(max(list2[lineCount-1]))
