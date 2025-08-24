import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

if N < 10:
    print(N)
else:
    num = 10
    while num <= N:
        N = ((N + num // 2) // num) * num
        num *= 10
    print(N)