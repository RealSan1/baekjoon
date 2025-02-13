import sys, itertools
input = sys.stdin.readline

while True:
    T = int(input())
    if T == 0:
        break
    
    arr = {}
    for _ in range(T):
        N, H = map(str, input().split())
        arr[N] = H

    big = max(arr.values())
    result = []
    sort = sorted(arr.items(), key=lambda x: x[1], reverse=True)
    for i,j in sort:
        if j == big:
            result.append(i)
        else:
            break

    print(*result)
        