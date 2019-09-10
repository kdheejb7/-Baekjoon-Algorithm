lineCount = int(input())
graph = []
ans = [[0 for _ in range(lineCount)] for _ in range(lineCount)]
q = []

def bfs(t):
    visit = []
    for index, value in enumerate(graph[t]):
        if value != 0:
            q.append(index)

    while q:
        node = q.pop(0)               #DFS로 구현 시 node = q.pop() 로만 바꿔주면 된다.
        if node not in visit:
            visit.append(node)
            q.extend([index for index,value in enumerate(graph[node]) if value != 0])

    return visit


for i in range(lineCount):
    graph.append(list(map(int,input().split())))

for i in range(lineCount):
    visit2 = bfs(i)
    for j in range(lineCount):
        if j in visit2:
            ans[i][j] = 1 

for i in range(lineCount):
    for j in range(lineCount):
        print(ans[i][j], end=" ")
    print()
