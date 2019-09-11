com_count = int(input())
input_count = int(input())
visited = [False for _ in range(com_count+1)]
adj = [[] for _ in range(com_count+1)]

def bfs(v):
    q = []
    q.append(v)
    visited[v] = True
    cnt = 0
    while q:
        v = q.pop()
        for e in adj[v]:
            if not visited[e]:
                visited[e] = True
                q.append(e)
                cnt += 1
    return cnt
for _ in range(input_count):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    
print(bfs(1))
