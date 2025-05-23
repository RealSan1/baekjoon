import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    A.sort()
    A = A[1:-1]
    if A[-1] - A[0] >= 4:
        print('KIN')
    else:
        print(sum(A))
    