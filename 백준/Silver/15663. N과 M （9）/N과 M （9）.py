import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = list(itertools.permutations(arr, M))
result = sorted(set(result))
for i in result:
    print(*i)
