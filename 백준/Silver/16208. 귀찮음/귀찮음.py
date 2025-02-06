import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = 0

arr.sort()
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        result += arr[i] * arr[j]

print(result)