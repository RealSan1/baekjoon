import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = list(map(int, input().split()))

dit = {}
index = 0
result = []
for i in arr:
    if i in dit:
        dit[i][0] += 1
    else:
        dit[i] = [1, index]
        index += 1

dit = sorted(dit.items(), key=lambda x: (-x[1][0], x[1][1]))

for i, j in dit:
    result.extend([i] * j[0])

print(*result)