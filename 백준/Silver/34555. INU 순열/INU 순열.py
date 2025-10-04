import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = []
l, r = (N+1)//2, (N+1)//2 + 1 
res.append(l)

for i in range(1, N):
    if i % 2 == 1:
        res.append(l + (i+1)//2)
    else:
        res.append(l - i//2)

print(*res)
