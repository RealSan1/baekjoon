import sys
input = sys.stdin.readline

N = int(input())
hills = [int(input()) for _ in range(N)]
hills.sort()

min_cost = float('inf')

for low in range(84):
    high = low + 17
    cost = 0

    for h in hills:
        if h < low:
            cost += (low - h) ** 2 
        elif h > high:
            cost += (h - high) ** 2 

    min_cost = min(min_cost, cost)

print(min_cost)