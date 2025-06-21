import sys
input = sys.stdin.readline

A, B = map(str, input().split())
si = max(len(A), len(B))
A = A.zfill(si)
B = B.zfill(si)
A = int(A, base=2)
B = int(B, base=2)
print(bin(A+B)[2:])