import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A != B[:N]:
    print("NO")
    sys.exit(0)


cnt = defaultdict(int)
for x in A:
    cnt[x] += 1

ptr = 0

for x in B[N:]:
    if cnt[x] > 0:
        cnt[x] += 1
    else:
        if ptr >= N or A[ptr] != x:
            print("NO")
            sys.exit(0)
        cnt[x] += 1
        ptr += 1

print("YES")