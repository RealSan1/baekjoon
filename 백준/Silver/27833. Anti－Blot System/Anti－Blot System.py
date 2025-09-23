import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    input()
    num = list(map(str, input().split()))
    V = 0
    for i in num:
        if not i.isnumeric() and i not in ['+', '=']:
            break
        V += 1
        
    if V == 4:
        res = int(num[0]) + int(num[2])
        num[4] = res
        print(*num)
    
    elif V == 2:
        res = int(num[4]) - int(num[0])
        num[2] = res
        print(*num)
    
    elif V == 0:
        res = int(num[4]) - int(num[2])
        num[0] = res
        print(*num)