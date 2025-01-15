def dfs(graph, visited, person, depth):
    if depth == 2:
        return
    for nx in graph[person]:
        if not visited[nx]:
            visited[nx] = True
        dfs(graph, visited, nx, depth+1)

n = int(input())
m = int(input())
friends = [map(int, input().split()) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited[1] = True

for p1, p2 in friends:
    graph[p1].append(p2)
    graph[p2].append(p1)

dfs(graph, visited, 1, 0)

print(len(list(filter(lambda x:x==True, visited))) - 1)
