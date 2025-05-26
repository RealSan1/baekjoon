import sys
input = sys.stdin.readline

N = input().strip()
result = 1
prev = ''
for i in N:
    if i == 'c':
        gop = 26
        if prev == 'c':
            gop -= 1
    elif i == 'd':
        gop = 10
        if prev == 'd':
            gop -= 1
    result *= gop
    prev = i

print(result)