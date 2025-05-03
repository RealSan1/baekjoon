import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

median = A[N // 2] if N % 2 == 1 else A[N // 2 - 1]
print(median)