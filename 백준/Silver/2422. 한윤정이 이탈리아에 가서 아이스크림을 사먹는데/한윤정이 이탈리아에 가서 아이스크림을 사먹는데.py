import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = set()
result = 0

for i in range(M):
    a, b = sorted(map(int, input().split()))
    arr.add((a,b))

for i in itertools.combinations(range(1, N + 1), 3):
    a, b, c = sorted(i)
    if (a, b) in arr or (a, c) in arr or (b, c) in arr:
        continue
    result += 1

print(result)