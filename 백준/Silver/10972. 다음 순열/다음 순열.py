import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

i = N - 2
while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1

if i == -1:
    print(-1)
else:
    j = N - 1
    while arr[i] >= arr[j]:
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])

    print(*arr)