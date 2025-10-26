import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()
if N == 'M':
    print('MatKor')
elif N == 'W':
    print('WiCys')
elif N == 'C':
    print('CyKor')
elif N == 'A':
    print('AlKor')
elif N == '$':
    print('$clear')