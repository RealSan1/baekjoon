import math

N = int(input())
for i in range(N):
    r, n = map(int, input().split())
    result = math.comb(n,r)
    print(result)