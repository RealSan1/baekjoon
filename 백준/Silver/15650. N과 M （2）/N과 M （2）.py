import itertools

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

nCr = itertools.combinations(arr, M)
nCr = list(nCr)

for i in nCr:
    print(' '.join(map(str, i)))