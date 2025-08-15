import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    num = int(input())
    res = 0
    for i in range(1, num+1):
        if i % 2 != 0:
            res += i
    print(res)