import sys
i = 2
var = 1
A, B = map(int, sys.stdin.readline().split())
while True: #소인수 분해
    if i > A and i > B:
        print(var)
        var *= A
        var *= B
        i = 2
        print(var)
        break

    if A % i == 0 and B % i == 0:
        var *= i
        A = A // i
        B = B // i
        i = 2
    else:
        i += 1