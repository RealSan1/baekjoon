import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
if len(arr) % 2 == 0:
    num = len(arr) // 2
    mid = (arr[num] + arr[num-1]) / 2
    print(f"{sum(arr) / len(arr):.6f}")
    print(f"{mid:.6f}")
else:
    num = len(arr) // 2
    print(f"{sum(arr) / len(arr):.6f}")
    print(f"{arr[num]:.6f}")