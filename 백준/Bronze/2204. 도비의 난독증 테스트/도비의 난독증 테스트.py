import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    arr = []
    ori = []
    for i in range(N):
        A = input().strip()
        arr.append([A.lower(), i])
        ori.append([A, i])
    arr.sort()
    V = arr[0][1]
    for i, j in ori:
        if j == V:
            print(i)
            break
    