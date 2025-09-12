import sys, copy
input = lambda: sys.stdin.readline().rstrip()

V = int(input())
for _ in range(V):
    T = list(input())
    A = int(len(T) ** 0.5)
    arr = []
    res = ''
    for i, j in enumerate(T):
        if len(res) % A == 0 and len(res) != 0:
            arr.append(list(res))
            res = ''
            res += j
        else:
            res += j

    arr.append(list(res))
    res = copy.deepcopy(arr)
    N = len(arr)

    for i in range(N):
        for j in range(N):
            res[N-1-j][i] = arr[i][j]

    num = ''
    for i in res:
        for j in i:
            num += j

    print(num)