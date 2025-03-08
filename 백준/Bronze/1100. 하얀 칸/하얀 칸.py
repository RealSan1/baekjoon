import sys
input = sys.stdin.readline

chess = []
for _ in range(8):
    chess.append(input().strip())


result = 0
for i in range(len(chess)):
    if i % 2 != 0: # 홀
        for j in range(8):
            if chess[i][j] == 'F' and j % 2 != 0:
                result += 1
    else: # 짝
        for j in range(8):
            if chess[i][j] == 'F' and j % 2 == 0:
                result += 1

print(result)