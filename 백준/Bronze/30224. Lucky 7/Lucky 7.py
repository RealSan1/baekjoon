import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
Bool = False
if str(N).count('7') > 0:
    Bool = True

if Bool and N % 7 == 0:
    print(3)
elif Bool and N % 7 != 0:
    print(2)
elif not Bool and N % 7 == 0:
    print(1)
elif not Bool and N % 7 != 0:
    print(0)