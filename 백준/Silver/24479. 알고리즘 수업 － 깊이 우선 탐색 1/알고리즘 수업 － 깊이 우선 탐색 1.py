import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N+1)]
enter = [0] * (N+1)
DFS = 1
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    graph[i].sort()
def dfs(node):
    global DFS
    enter[node] = DFS
    DFS += 1
    for i in graph[node]:
        if enter[i] == 0:
            dfs(i)

dfs(V)

for i in enter[1:]:
    print(i)