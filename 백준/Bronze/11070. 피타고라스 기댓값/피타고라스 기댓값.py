import sys
input = lambda: sys.stdin.readline().rstrip()

for t in range(int(input())):
    N, M = map(int, input().split())
    MAX = 0
    MIN = sys.maxsize
    arr = {i : [0, 0] for i in range(1, N+1)}
    for m in range(M):
        a, b, p, q = map(int, input().split())
        arr[a][0] += p
        arr[a][1] += q
        arr[b][0] += q
        arr[b][1] += p

    for S, A in arr.items():
        GET = A[0]
        PUT = A[1]
        if GET == 0 and PUT == 0:
            num = 0
        elif GET == 0:
            num = 0
        else:
            num = int((GET ** 2) / ((GET ** 2) + (PUT ** 2)) * 1000)
        MAX = max(MAX, num)
        MIN = min(MIN, num)

    print(MAX)
    if MIN == sys.maxsize:
        print(0)
    else:
        print(MIN)