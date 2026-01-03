import sys
input = lambda: sys.stdin.readline().rstrip()

for i in range(int(input())):
    N = int(input())

    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(4)
    elif N == 4:
        print(7)
    elif N == 5:
        print(13)
    elif N == 6:
        print(24)
    elif N == 7:
        print(44)
    elif N == 8:
        print(81)
    elif N == 9:
        print(149)
    elif N == 10:
        print(274)
    elif N == 11:
        print(504)