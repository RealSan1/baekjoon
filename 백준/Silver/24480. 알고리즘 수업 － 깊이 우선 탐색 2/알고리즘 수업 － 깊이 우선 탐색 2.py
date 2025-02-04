import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, R = map(int, input().split())
count = 1
graph = [[] for i in range(M+1)]
visited = [False] * (M+1)
result = [0] * (M+1)

for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(len(graph)):
    graph[i].sort(reverse=True)

def dfs(node):
    global count
    visited[node] = True
    result[node] = count
    for i in graph[node]:
        if not visited[i]:
            count += 1
            dfs(i)
dfs(R)

for i in result[1:]:
    print(i)