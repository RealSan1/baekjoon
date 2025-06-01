import sys
input = sys.stdin.readline

N = int(input())
card = [i for i in range(1, N+1)]
result = []
while True:
    try:
        result.append(card.pop(0))
        result.append(card.pop(0))
        card.append(result[-1])
        result.pop()
    except:
        break

print(*result)
