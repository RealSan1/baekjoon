import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1
result = 0

while end > start:
    if arr[start] + arr[end] <= K:
        result += 1
        start += 1
        end -= 1
    else:
        end -= 1

print(result)