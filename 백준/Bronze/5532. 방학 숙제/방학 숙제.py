import sys, math
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
M = math.ceil(B / D)
K = math.ceil(A / C)
T = max(M, K)
print(L - T)