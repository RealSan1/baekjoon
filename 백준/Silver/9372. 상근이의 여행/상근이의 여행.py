T = int(input())
for t in range(T):
    N, M = map(int, input().split()) # 국가, 비행기
    graph = [[] for i in range(N+1)]

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    print(N-1)