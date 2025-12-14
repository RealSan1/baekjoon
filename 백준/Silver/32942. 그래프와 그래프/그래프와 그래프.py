import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())
arr = {i : [] for i in range(1, 11)}

for x in range(1, 11):
    for y in range(1, 11):
        if x * A + y * B == C:
            arr[x] += [y]

for i, j in arr.items():
    if j:
        print(*j)
    else:
        print(0)