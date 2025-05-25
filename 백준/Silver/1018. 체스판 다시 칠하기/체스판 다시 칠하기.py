import sys
input = sys.stdin.readline

def reChess(chess, start_x, start_y):
    result = 0
    V = sys.maxsize
    for i in range(8):
        for j in range(8):
            cur = chess[start_x + i][start_y + j]
            if cur == 'B' and j % 2 == 0 and i % 2 == 0:
                result += 1
            elif cur == 'W' and j % 2 == 1 and i % 2 == 0:
                result += 1
            elif cur == 'W' and j % 2 == 0 and i % 2 == 1:
                result += 1
            elif cur == 'B' and j % 2 == 1 and i % 2 == 1:
                result += 1
    V = min(result, V)

    result = 0
    for i in range(8):
        for j in range(8):
            cur = chess[start_x + i][start_y + j]
            if cur == 'W' and j % 2 == 0 and i % 2 == 0:
                result += 1
            elif cur == 'B' and j % 2 == 1 and i % 2 == 0:
                result += 1
            elif cur == 'B' and j % 2 == 0 and i % 2 == 1:
                result += 1
            elif cur == 'W' and j % 2 == 1 and i % 2 == 1:
                result += 1
    V = min(result, V)
    return V

chess = []
N, M = map(int, input().split())
for _ in range(N):
    chess.append(input().strip())

min_paint = sys.maxsize
for i in range(N - 7):
    for j in range(M - 7):
        min_paint = min(min_paint, reChess(chess, i, j))

print(min_paint)
