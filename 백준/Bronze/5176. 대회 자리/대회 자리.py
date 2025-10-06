import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
for _ in range(K):
    P, M = map(int, input().split())
    arr = {}
    res = 0
    for i in range(P):
        N = int(input())
        if N in arr:
            res += 1
        else:
            arr[N] = 1
    print(res)
    