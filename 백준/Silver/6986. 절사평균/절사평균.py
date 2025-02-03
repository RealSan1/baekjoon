import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _ in range(N):
    A = float(input())
    arr.append(A)

arr.sort()
A = sum(arr[K:N-K]) / (N - 2 * K)
print("%.2f" %(A+1e-8))

B = (sum(arr[K:N-K])+arr[K]*K+arr[N-K-1]*K)/N
print("%.2f" %(B+1e-8))