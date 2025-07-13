import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = input().strip()
    Bool = True
    res = int(num) ** (1/2)
    if res - round(res) != 0:
        Bool = False
    
    num = num[::-1]
    res = int(num) ** (1/2)
    if res - round(res) != 0:
        Bool = False
    
    if Bool:
        print("YES")
    else:
        print("NO")
