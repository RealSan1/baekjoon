import sys
input = lambda: sys.stdin.readline().rstrip()

C = 0
while True:
    N = int(input())
    C += 1
    if N == 0:
        break
    arr = {}
    Glist = []
    for _ in range(N):
        Glist.append(input())

    for i in range(2*N - 1):
        num, V = map(str, input().split())
        num = int(num) - 1
        if num in arr:
            arr[num] += 1
        else:
            arr[num] = 1
    A = sorted(arr.items(), key=lambda x: x[1])[0][0]
    print(C, Glist[A])