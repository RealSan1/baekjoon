import sys
input = lambda: sys.stdin.readline().rstrip()

arr = [1] * 81
arr[2] = 2
for i in range(2, 81):
    arr[i] = arr[i-2] + arr[i-1]

N = int(input())
if N == 1:
    print(4)
else:
    print((arr[N-1] + arr[N-2]) * 2 + arr[N-1] * 2)