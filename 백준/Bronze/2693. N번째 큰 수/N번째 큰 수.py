import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = list(map(int, input().split()))
    P.sort()
    print(P[7])
