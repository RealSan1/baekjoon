import sys
input = sys.stdin.readline

while True:
    R, X = map(int, input().split())
    if R == 0 and X == 0:
        break
    
    arr = []
    for _ in range(R):
        arr.append(input().strip())

    result = []
    for i in range(R):
        row = []
        for j in range(X):
            count = 0
            if arr[i][j] == '*':
                row.append('*')
            else:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        ni = i + x
                        nj = j + y
                        if 0 <= ni < R and 0 <= nj < X:
                            if arr[ni][nj] == '*':
                                count += 1
                row.append(str(count))
        result.append(row)

    for i in range(R):
        for j in range(X):
            print(result[i][j], end="")
        print()

        