import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    adam = input()
    res = 0
    for i in adam:
        if i == 'D':
            break
        res += 1
    print(res)