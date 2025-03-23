import sys
input =  sys.stdin.readline

N = int(input())
for i in range(N):
    if i % 2 == 0:
        star = ''
        for i in range(N):
            star += '*'
            star += ' '
        print(star)
    else:
        star = ''
        for i in range(N):
            star += ' '
            star += '*'
        print(star)