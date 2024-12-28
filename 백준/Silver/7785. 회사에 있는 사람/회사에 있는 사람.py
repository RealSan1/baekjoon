N = int(input())
arr = {}

for i in range(N):
    A = input().split()
    if A[1] == 'enter':
        arr[A[0]] = 1
    elif A[1] == 'leave':
        arr[A[0]] = 0

for key, value in sorted(arr.items(), reverse=True):
    if value == 1:
        print(key)