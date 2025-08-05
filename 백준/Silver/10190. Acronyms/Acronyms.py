import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    num = list(map(str, input().split()))
    N = int(num[1])
    num = num[0]
    arr = []
    for _ in range(N):
        ACR = input()
        res = list(ACR.split(' '))
        if len(res) == len(num):
            Bool = True
            for i, j in enumerate(res):
                if j[0] != num[i]:
                    Bool = False
            
            if Bool:
                arr.append(ACR)
    print(num)
    for re in arr:
        print(re)