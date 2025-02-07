import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = set(arr)
sort = sorted(arr, reverse=False)

result = list(itertools.combinations_with_replacement(sort, M))

for i in result:
    print(*i)