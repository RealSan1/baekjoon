import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = arr + arr  

current_sum = sum(arr[:K])
max_sum = current_sum

for i in range(1, N):
    current_sum += arr[i + K - 1] 
    current_sum -= arr[i - 1]
    max_sum = max(max_sum, current_sum)

print(max_sum)
