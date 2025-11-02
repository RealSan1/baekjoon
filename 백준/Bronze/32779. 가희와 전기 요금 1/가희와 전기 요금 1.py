import sys
input = lambda: sys.stdin.readline().rstrip()

cost = 105.6 / 60 / 1000
Q = int(input())
for _ in range(Q):
    A, M = map(int, input().split())
    print(int(cost * A * M))