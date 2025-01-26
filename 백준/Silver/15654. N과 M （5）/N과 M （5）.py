import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = list(itertools.permutations(arr, M))

result.sort()
for i in result:
    print(*i)