import sys
input = lambda: sys.stdin.readline().rstrip()

H, W = map(int, input().split())
arr = []
for i in range(H):
    arr.append(input())

res = []
for i in range(H):
    Bool = False
    num = 0
    V = []
    for j in range(W):
        if arr[i][j] == 'c':
            Bool = True
            num = 0
            V.append(num)
            continue
        
        if Bool:
            num += 1
            V.append(num)
        else:
            V.append(-1)

    res.append(V)

for i in res:
    print(*i)