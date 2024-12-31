T = int(input())
for _ in range(T):
    RY = 0
    RK = 0
    for i in range(9):
        Y, K = map(int, input().split())
        RY += Y
        RK += K
    if RY > RK:
        print('Yonsei')
    elif RY == RK:
        print('Draw')
    elif RY < RK:
        print('Korean')