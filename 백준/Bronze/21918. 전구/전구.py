import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(M):
    A, l, r = map(int, input().split())
    l = l-1
    if A == 1:
        arr[l] = r

    elif A == 2:
        for i in range(l, r):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0

    elif A == 3:
        for t in range(l, r):
            arr[t] = 0

    elif A == 4:
        for t in range(l, r):
            arr[t] = 1

print(*arr)