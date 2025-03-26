import sys, itertools
import itertools

input = sys.stdin.readline
C, N = map(int, input().split())
W = [int(input()) for _ in range(N)]

max_weight = 0

for r in range(1, N + 1):
    for subset in itertools.combinations(W, r):
        total = sum(subset)
        if total <= C:
            max_weight = max(max_weight, total)

print(max_weight)
