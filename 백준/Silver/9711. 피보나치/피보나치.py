import sys
input = sys.stdin.readline

arr = [0] * 10001
arr[0], arr[1] = 1, 1

for i in range(2, 10001):
    arr[i] = arr[i-2] + arr[i-1]

T = int(input())
for i in range(T):
    P, Q = map(int, input().split())
    print(f"Case #{i+1}: {arr[P-1] % Q}")