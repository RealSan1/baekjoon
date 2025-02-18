import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

result = set(itertools.combinations(arr, M)) 

for i in sorted(result):
    print(*i)
