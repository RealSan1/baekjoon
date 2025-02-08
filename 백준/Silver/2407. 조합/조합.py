import sys, math
input = sys.stdin.readline

N, M = map(int, input().split())

result = math.comb(N,M)
print(result)