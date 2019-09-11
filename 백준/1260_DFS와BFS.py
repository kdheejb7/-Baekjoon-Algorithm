v,e,start = map(int,input().split())
visited = [False for _ in range(v+1)]
adj = [[] for _ in range(v+1)]
for _ in range(e):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in adj:
    i.sort()
bfs_ans = []
def bfs(s):
    q = []
    visited = [False for _ in range(v+1)]
    visited[s] = True
    q.append(s)
    bfs_ans.append(s)
    while q:
        temp = q.pop(0)
        for i in adj[temp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                bfs_ans.append(i)
   

dfs_ans = []
def dfs(s):
    visited[s] = True
    dfs_ans.append(s)
    for e in adj[s]:
        if not visited[e]:
            dfs(e)
    
bfs(start)
dfs(start)
print(*dfs_ans,sep=' ')   
print(*bfs_ans,sep=' ')
​
