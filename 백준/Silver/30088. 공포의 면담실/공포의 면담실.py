N = int(input())
arr = []
for i in range(N):
    A = list(map(int, input().split()))
    arr.append(sum(A[1:]))

arr.sort()
for i in range(1, len(arr)):
    arr[i] += arr[i-1]

print(sum(arr))