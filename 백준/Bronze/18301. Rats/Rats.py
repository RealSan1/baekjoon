import sys, math
input = sys.stdin.readline

N1, N2, N12 = map(int, input().split())

N = math.floor((N1 + 1) * (N2 + 1) / (N12 + 1) -1)
print(N)