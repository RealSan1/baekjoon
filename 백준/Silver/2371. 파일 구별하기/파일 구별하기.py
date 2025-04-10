import sys
input = sys.stdin.readline

T = int(input())
result = 0
for _ in range(T):
    arr = list(map(int, input().split()))
    result = max(len(arr[:-1]), result)

print(result)