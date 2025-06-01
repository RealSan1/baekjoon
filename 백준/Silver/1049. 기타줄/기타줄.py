import sys
input = sys.stdin.readline

N, M = map(int, input().split())
minP = sys.maxsize
minE = sys.maxsize

for _ in range(M):
    A, B = map(int, input().split())
    minP = min(minP, A)
    minE = min(minE, B)

cost1 = ((N + 5) // 6) * minP  
cost2 = N * minE               
cost3 = (N // 6) * minP + (N % 6) * minE

print(min(cost1, cost2, cost3))