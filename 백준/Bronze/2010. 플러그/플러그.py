import sys
input = sys.stdin.readline

N = int(input())
res = 1
for _ in range(N):
    A = int(input())
    res += A
    res -= 1

print(res)