import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    num = list(map(int, input().split()))
    print(*num)
    if 17 in num and 18 in num:
        print("both")
    elif 17 in num:
        print("zack")
    elif 18 in num:
        print("mack")
    else:
        print("none")

    if t != T-1:
        print()