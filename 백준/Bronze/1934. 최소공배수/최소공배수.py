import sys
T = int(sys.stdin.readline())
i = 2
for t in range(T):
    var = 1
    A, B = map(int, sys.stdin.readline().split())
    while True: #소인수 분해
        if i > A and i > B:
            var *= A
            var *= B
            i = 2
            break

        if A % i == 0 and B % i == 0:
            var *= i
            A = A // i
            B = B // i
            i = 2
        else:
            i += 1
    
    print(var)
