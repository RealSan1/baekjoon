import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
P = []
Q = []
for p in range(N):
    x, y = map(int, input().split())
    P.append([x, y])

for q in range(M):
    x, y = map(int, input().split())
    Q.append([x, y])

res = 0
for Px, Py, in P:
    for Qx, Qy in Q:
        res = max(res, ((Px - Qx) ** 2 + (Py - Qy) ** 2))

print(res)