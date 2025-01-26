N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []

for _ in range(M):
    B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for l in range(M):
            result[i][j] += A[i][l]*B[l][j]

for r in result:
    print(*r)