import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N -= 1
M -= 1
arr = []
for i in range(10):
    arr.append(input())

boomX = [False] * 10
boomY = [False] * 10
for x in range(10):
    for y in range(10):
        if 'o' == arr[x][y]:
            boomX[x] = True
            boomY[y] = True

ans = float('inf')

for i in range(10):
    for j in range(10):
        if not boomX[i] and not boomY[j]:
            dist = abs(N - i) + abs(M - j)
            ans = min(ans, dist)

print(ans)