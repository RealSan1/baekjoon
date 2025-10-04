import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = N
N = N // 2 + 1
res = []
for i in range(N):
    res.append(N+i)
    res.append(N-1-i)

res = res[:-1]
if A % 2 == 0:
    print(*res[:-1])
else:
    print(*res)