import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())
res = set()
for _ in range(N):
    std = int(input())
    i = 1
    while True:
        if std * i <= C:
            res.add(std * i)
        else:
            break
        i += 1

if res:
    print(len(res))
else:
    print(0)