import sys, decimal
input = lambda: sys.stdin.readline().rstrip()

A, B, C = map(decimal.Decimal, input().split())
print(A * B / C)
