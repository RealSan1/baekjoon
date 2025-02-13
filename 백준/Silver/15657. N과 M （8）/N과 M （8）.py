import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = list(itertools.combinations_with_replacement(arr, M))

for i in result:
    print(*i)