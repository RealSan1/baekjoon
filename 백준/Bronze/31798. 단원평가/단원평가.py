import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
if A == 0:
    print(C*C - B)
elif B == 0:
    print(C*C - A)
elif C == 0:
    print(int((A + B) ** 0.5))
