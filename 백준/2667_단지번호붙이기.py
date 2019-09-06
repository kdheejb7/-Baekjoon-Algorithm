n = int(input())
map_ = [[] for _ in range(n)]
for i in range(n):
    map_[i] = list(map(int, input()))
    
def bfs(t1,t2):
    q = []
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    q.append([t1,t2])
    count = 0
    while q:
        r,c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nc>=0 and nc<n and nr>=0 and nr<n and map_[nr][nc]==1:
                q.append([nr,nc])
                map_[nr][nc] = 0
                count += 1
    return count if count else count+1

count_list = []
for i in range(n):
    for j in range(n):
        if map_[i][j] != 0:
            count_list.append(bfs(i,j))
count_list.sort()
print(len(count_list))
print(*count_list,sep="\n")
