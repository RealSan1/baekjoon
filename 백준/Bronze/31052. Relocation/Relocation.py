import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
loc = list(map(int, input().split()))
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        loc[A-1] = B
    else:
        print(abs(loc[A-1]-loc[B-1]))