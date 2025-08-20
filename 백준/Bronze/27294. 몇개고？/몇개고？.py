import sys
input = lambda: sys.stdin.readline().rstrip()

T, S = map(int, input().split())
if T <= 11:
    print(280)
elif T >= 12 and T <= 16:
    if S == 1:
        print(280)
    else:
        print(320)
else:
    print(280)