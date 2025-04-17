import sys
input = sys.stdin.readline

N, M = map(int, input().split())
V, P, S = map(int, input().split())
jewon = V + P + S
arr = []
result = [0]
for i in range(N):
    V1, P1, S1 = map(int, input().split())
    if V1 + P1 + S1 > jewon:
        continue

    arr.append([i+1, V1 + P1 + S1])

arr = sorted(arr, key=lambda x: -x[1])

for i,j in arr:
    if len(result) < M:
        result.append(i)

print(*result)