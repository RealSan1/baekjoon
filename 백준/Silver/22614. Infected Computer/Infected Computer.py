import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    
    arr, res = [], []
    for _ in range(M):
        T, S, D = map(int, input().split())
        arr.append([T, S, D])
    arr = sorted(arr, key=lambda x: x[0])
    res.append(1)
    for T, S, D in arr:
        if D not in res and S in res:
            res.append(D)

    print(len(res))
