import sys
input = sys.stdin.readline

N = int(input())
A = []
result = 0
for _ in range(N):
    A.append(int(input()))

M = int(input())
for _ in range(M):
    B = int(input())
    result += A[B-1]

print(result)