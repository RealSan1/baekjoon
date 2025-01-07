import sys

N, M = map(int,sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
result = 0

for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

    
def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)


for i in range(1, N+1):
    if visited[i] == False:
        result +=1
        dfs(i)

print(result)