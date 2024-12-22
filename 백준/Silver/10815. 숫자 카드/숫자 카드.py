N = int(input())
상근 = set(input().split())
M = int(input())
카드 = input().split()

result = []
for i in 카드:
    if i in 상근:
        result.append(1)
    else:
        result.append(0)

print(*result)