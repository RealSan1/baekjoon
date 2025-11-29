import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    num = list(map(str, input().split()))
    res = ''
    for i in num:
        if len(i) == 4:
            res += '****'
        else:
            res += i
        res += ' '
    print(res)
    print()