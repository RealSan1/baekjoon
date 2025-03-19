import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
pre = [0] * (N+1)
pre[0] = arr[0]

for i in range(1, N+1):
    pre[i] = pre[i-1] + arr[i-1]

for i in range(Q):
    A, B = map(int, input().split())
    print(pre[B] - pre[A-1])
