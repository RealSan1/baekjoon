import sys
input = sys.stdin.readline

P = [0] * 102
P[0], P[1], P[2], P[3], P[4] = 1, 1, 1, 2, 2
for i in range(5, 102):
    P[i] = P[i-2] + P[i-3]

N = int(input())
for _ in range(N):
    print(P[int(input())-1])