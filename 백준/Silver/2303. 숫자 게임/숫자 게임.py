import sys, itertools
input = sys.stdin.readline

N = int(input())
res = []
for n in range(N):
    A = list(map(int, input().split()))
    M = 0
    for i in itertools.permutations(A, 3):
        M = max(sum(i)%10, M)
    res.append([n+1, M])

print(sorted(res, key=lambda x: (-x[1], -x[0]))[0][0])