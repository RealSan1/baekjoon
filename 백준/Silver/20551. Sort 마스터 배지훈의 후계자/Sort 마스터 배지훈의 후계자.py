import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = []
for n in range(N):
    arr += [int(input())]

arr.sort()

for m in range(M):
    num = int(input())
    start = 0
    end = N - 1
    idx = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= num:
            end = mid - 1

            if arr[mid] == num:
               idx = mid

        else:
            start = mid + 1

    print(idx)