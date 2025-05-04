import sys, itertools
input = sys.stdin.readline

N, S = map(int, input().split())
exclude = set(map(int, input().split())) if S != 0 else set()

arr = [i for i in range(1, 1002) if i not in exclude]
arr.sort(reverse=True)

result = sys.maxsize
for x,y,z in itertools.combinations_with_replacement(arr, 3):
    product = x * y * z
    diff = abs(N - product)
    if diff < result:
        result = diff
        if result == 0:
            break

print(result)