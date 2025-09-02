import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = input()
    arr = []
    num = 1
    res = ''
    if len(N) != 1:
        for i in range(1, len(N)):
            if N[i-1] == N[i]:
                num += 1
            else:
                arr.append([num, int(N[i-1])])
                num = 1
        arr.append([num, int(N[i])])
    else:
        arr.append([num, int(N)])
        
    for i, j in arr:
        res += str(i)
        res += str(j)

    print(res)