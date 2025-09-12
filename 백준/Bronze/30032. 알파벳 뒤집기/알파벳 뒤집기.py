import sys
input = lambda: sys.stdin.readline().rstrip()

N, D = map(int, input().split())
for _ in range(N):
    num = input()
    res = ''
    if D == 1:
        for i in num:
            if i == 'd':
                res += 'q'
            elif i == 'b':
                res += 'p'
            elif i == 'q':
                res += 'd'
            elif i == 'p':
                res += 'b'

    else:
        for i in num:
            if i == 'd':
                res += 'b'
            elif i == 'b':
                res += 'd'
            elif i == 'q':
                res += 'p'
            elif i == 'p':
                res += 'q'
    
    print(res)