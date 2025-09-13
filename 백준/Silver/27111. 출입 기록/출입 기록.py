import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = set()
res = 0
for _ in range(N):
    A, B = map(int, input().split())
    if B == 1:
        if A in arr:
            res += 1
        else:
            arr.add(A)
    else:
        if A in arr:
            arr.remove(A)
        else:
            res += 1

res += len(arr)
print(res)
