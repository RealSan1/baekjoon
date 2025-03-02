import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
hap = sum(arr)
result = 0
for i in range(N-1):
    hap -= arr[i]
    result += hap * arr[i]
    
print(result)