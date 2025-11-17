import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()

num = N.split('-')
res = sum(map(int, num[0].split('+')))
for p in num[1:]:
    res -= sum(map(int, p.split('+')))

print(res)
