import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(int, input().split())
res = (B / A) * 3
print(int(res*C))