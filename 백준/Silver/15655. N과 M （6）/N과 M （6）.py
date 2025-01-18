import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

A = itertools.combinations(arr, M)

for i in A:
    print(" ".join(map(str, i)))