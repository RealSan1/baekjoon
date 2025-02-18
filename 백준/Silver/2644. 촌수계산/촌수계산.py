import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
T = int(input())

graph = [[] for i in range(n+1)]
vistied = [False] * (n+1)

for _ in range(T):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node, count):
    vistied[node] = True
    if node == B:
        return count

    for i in graph[node]:
        if not vistied[i]:
            result = dfs(i, count+1)
            if result is not None:
                return result
    return None

count = dfs(A,0)

if count == None:
    print(-1)
else:
    print(count)