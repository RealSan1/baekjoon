import sys, itertools
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = list(itertools.product(arr, repeat=M))
result = set(result)

for i in sorted(result):
    print(*i)