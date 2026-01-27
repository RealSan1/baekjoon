import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    num = list(map(int, input().split()))
    res = 0
    MIN = sys.maxsize
    for i in num:
        if i % 2 == 0:
            res += i
            MIN = min(i, MIN)
    
    print(res, MIN)