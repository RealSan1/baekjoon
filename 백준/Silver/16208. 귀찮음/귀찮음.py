import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = 0

arr.sort()
hap = sum(arr)
for i in range(N-1):
    hap -= arr[i]
    result += arr[i] * hap

print(result)