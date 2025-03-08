import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
prefix_sum = 0

for i in range(N):
    result = (result + arr[i] * prefix_sum) % 1000000007
    prefix_sum = (prefix_sum + arr[i]) % 1000000007

print(result)