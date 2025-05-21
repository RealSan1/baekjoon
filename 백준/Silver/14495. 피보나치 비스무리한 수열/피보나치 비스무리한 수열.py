import sys
input = sys.stdin.readline

arr = [0] * 120
arr[0], arr[1], arr[2] = 1, 1, 1
for i in range(3, 120):
    arr[i] = arr[i-1] + arr[i-3]

N = int(input())
print(arr[N-1])