r_, c_ = map(int, input().split())
maze = [[0]*(c_) for row in range(r_)]
visited = maze.copy()

def dfs():
    q = []
    q.append([0,0,1])
    dc = [-1,0,1,0]
    dr = [0,-1,0,1]
    while q:
        r, c, count = q.pop(0)
        if r == r_-1 and c == c_-1:
            print(count)
            return 
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if nc>=0 and nr>=0 and nc<c_ and nr<r_ and maze[nr][nc] == 1 and visited[nr][nc]==0:
                q.append([nr,nc,count+1])
                visited[nr][nc] = 1
    

for i in range(r_):
    maze[i] = list(map(int,input()))
dfs()

