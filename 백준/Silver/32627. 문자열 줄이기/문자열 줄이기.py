import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
S = list(input())

cnt = Counter(sorted(S)[:M])

res = []
for c in S:
    if cnt[c] > 0:
        cnt[c] -= 1
    else:
        res.append(c)

print(''.join(res))