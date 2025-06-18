import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # 세로 가로
    if N <= 11 or M <= 3:
        print(-1)
    else:
        res = (11 * M) + 4
        print(res)