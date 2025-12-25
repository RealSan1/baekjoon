import sys
input = sys.stdin.readline

N = int(input())
res = 0

while N != 1:
    if N % 2 != 0:
        N = (N * 3) + 1
    else:
        N = N / 2
    res += 1

print(res)