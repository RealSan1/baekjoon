import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

res = sys.maxsize
for i in range(N-1):
    res = min(res, abs(arr[i] - arr[i+1]))

print(res)