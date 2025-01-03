T = int(input()) # 컴퓨터 수
F = int(input()) # 연결된 네트워크 수

graph = [[] for _ in range(T+1)]
visited = [False] * (T+1)

for _ in range(F):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

result = 0
def dfs(node):
    global result
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            result += 1
            dfs(i)

dfs(1) # 1번 node부터 시작
print(result)