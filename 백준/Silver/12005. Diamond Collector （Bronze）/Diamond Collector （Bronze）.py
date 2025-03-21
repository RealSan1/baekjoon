import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

big = 0
left = 0
for right in range(N):
    while arr[right] - arr[left] > K:
        left += 1
    big = max(big, right - left + 1)

print(big)