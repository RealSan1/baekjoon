import sys, math
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for _ in range(t):
    n = int(input())
    for i in str(math.factorial(n))[::-1]:
        if i != '0':
            print(i)
            break