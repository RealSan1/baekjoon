import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    res = 0
    for i in range(N, 0, -1):
        res += i**2
    print(res)