import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for n in range(N):
    V = int(input())
    arr = {}
    for v in range(V):
        S = int(input())
        if S in arr:
            arr[S] += 1
        else:
            arr[S] = 1
    print(sorted(arr.items(), key=lambda x: (-x[1], x[0]))[0][0])