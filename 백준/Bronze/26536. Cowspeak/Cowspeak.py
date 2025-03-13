import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sound = list(map(str, input().strip().split()))
    result = ''
    for i in sound:
        M = 0
        O = 0
        for j in i:
            if j == 'M':
                M += 1
            elif j == 'O':
                O += 1
        result += chr(int(hex(M)[2:] + hex(O)[2:], base=16))
    print(result)
        