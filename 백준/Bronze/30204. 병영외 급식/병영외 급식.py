import sys
input = sys.stdin.readline

N, X = map(int, input().split())
P = list(map(int, input().split()))

if sum(P) % X == 0:
    print(1)
else:
    print(0)