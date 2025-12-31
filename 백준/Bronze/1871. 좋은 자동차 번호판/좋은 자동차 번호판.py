import sys
input = lambda: sys.stdin.readline().rstrip()


for t in range(int(input())):
    N = input().split("-")
    res = ((ord(N[0][0]) % 65) * 26**2) + ((ord(N[0][1]) % 65) * 26) + (ord(N[0][2]) % 65) - int(N[1])
    if abs(res) <= 100:
        print('nice')
    else:
        print('not nice')
    