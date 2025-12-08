import sys
input = lambda: sys.stdin.readline().rstrip()

X, Y, Z = map(int, input().split())
U, V, W = map(int, input().split())

print(X*U//100 + Y*V//50 + Z*W//20)