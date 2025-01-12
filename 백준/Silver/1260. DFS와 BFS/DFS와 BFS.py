from collections import deque
N, M, V = map(int, input().split())
DFS = []
BFS = []
graph = [[] for i in range(N+1)]


for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    graph[A].sort()

    graph[B].append(A)
    graph[B].sort()
    


def dfs(node):
    enter[node] = True
    DFS.append(node) # 방문
    for i in graph[node]:
        if not enter[i]:
            dfs(i)


def bfs(node):
    queue = deque([node])
    enter[node] = True

    while queue:
        v = queue.popleft()
        BFS.append(v) # 방문
        for i in graph[v]:
            if not enter[i]:
                queue.append(i)
                enter[i] = True

enter = [False] * (N+1)
dfs(V)
print(*DFS)

enter = [False] * (N+1)
bfs(V)
print(*BFS)