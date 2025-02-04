import sys
import itertools
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
result = list(itertools.combinations_with_replacement(arr, M))

for i in result:
    print(*i)