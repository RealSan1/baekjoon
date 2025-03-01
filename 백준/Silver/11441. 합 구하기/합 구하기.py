import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
prefix = [0] * (N+1)
prefix[0] = arr[0]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

T = int(input())
for _ in range(T):
    I, J = map(int, input().split())
    print(prefix[J] - prefix[I-1])