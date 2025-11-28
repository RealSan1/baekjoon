import sys
input = lambda: sys.stdin.readline().rstrip()

M = int(input())
B = list(map(int, input().split()))

N = B[0]
num = [N]
while N < M:
    num.append(B[N])
    N += B[N]

print(*num)