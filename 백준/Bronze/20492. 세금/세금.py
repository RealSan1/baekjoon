import sys
input = sys.stdin.readline

N = int(input())
A = int(N * 0.78)
B = int(N * 0.8 + ((N * 0.2) * 0.78))
print(A, B)