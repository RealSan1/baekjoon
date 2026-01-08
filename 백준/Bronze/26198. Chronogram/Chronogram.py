import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    num = input()
    res = 0
    for i in num:
        if i.count('I') > 0:
            res += 1
        if i.count('V') > 0:
            res += 5
        if i.count('X') > 0:
            res += 10
        if i.count('L') > 0:
            res += 50
        if i.count('C') > 0:
            res += 100
        if i.count('D') > 0:
            res += 500
        if i.count('M') > 0:
            res += 1000
    print(res)