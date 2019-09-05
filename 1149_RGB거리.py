lineCount = int(input())
rgb = [[0 for col in range(3)] for row in range(lineCount)]
for i in range(lineCount):
    rgb[i][0],rgb[i][1],rgb[i][2] = map(int,input().split())
for i in range(1,lineCount):
    rgb[i][0] = min(rgb[i-1][1],rgb[i-1][2])+rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2])+rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1])+rgb[i][2]

print(min(rgb[lineCount-1]))
