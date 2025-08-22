import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = 0
for _ in range(N):
    D = int(input())
    if D % 2 != 0:
        res += 1
print(res)