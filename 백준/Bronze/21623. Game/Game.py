import sys
input = sys.stdin.readline

K, N = map(int, input().split())
start = N
rd = 0
nums = list(map(int, input().split()))

for idx, x in enumerate(nums, 1):
    if N - x >= 0:
        N -= x
    if N == 0:
        rd += 1
        if idx < K:
            N = start

print(rd)
print(N)
