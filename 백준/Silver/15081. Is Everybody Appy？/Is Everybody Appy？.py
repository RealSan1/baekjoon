import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
res = []
for i in range(T):
    kid = list(map(str, input().split()))
    for i in range(1, int(kid[0])+1):
        if kid[i] not in res:
            res.append(kid[i])
            break
print(*res)