import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

nPr = itertools.permutations(arr, M)

for i in nPr:
    print(*i)