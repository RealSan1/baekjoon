import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))

arr = []
P.sort(reverse=True)
for p in P:
    egg = N
    res = 0
    for i in P:
        if i >= p and egg != 0:
            res += p
            egg -= 1
    arr.append([p, res])

print(*sorted(arr, key=lambda x: -x[1])[0])