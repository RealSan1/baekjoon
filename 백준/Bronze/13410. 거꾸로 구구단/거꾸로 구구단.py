import sys
input = sys.stdin.readline

N, M = map(int, input().split())
big = 1
for i in range(1, M+1):
    A = str(N*i)
    A = A[::-1]
    big = max(big, int(A))

print(big)