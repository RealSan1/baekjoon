import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
A = A // 2
B = B // 2
print(min(A, B))