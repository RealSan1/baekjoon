import sys
input = sys.stdin.readline

T = int(input())
for V in range(T):
    K = int(input())
    N = int(input())

    arr = [[i for i in range(1, N+1)] for _ in range(K+1)]

    for i in range(1, K+1):
        for j in range(N):
            arr[i][j] = sum(arr[i-1][:j+1])

    print(arr[K][N-1])