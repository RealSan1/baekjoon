import sys, math
input = sys.stdin.readline

A = int(input())
W, V = map(int, input().split())

if A * V <= W:
    print(1)
else:
    print(0)