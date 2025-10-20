import sys
input = lambda: sys.stdin.readline().rstrip()

X = {}
Y = {}
for _ in range(3):
    A, B = map(int, input().split())
    if A in X:
        X[A] += 1
    else:
        X[A] = 1
    
    if B in Y:
        Y[B] += 1
    else:
        Y[B] = 1

res = []
for i, j in X.items():
    if j != 2:
        res.append(i)

for i, j in Y.items():
    if j != 2:
        res.append(i)

print(*res)