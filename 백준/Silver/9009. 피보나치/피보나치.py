import sys
input = lambda: sys.stdin.readline().rstrip()

fib = [1, 2]
while fib[-1] <= 1000000001:
    fib.append(fib[-1] + fib[-2])

def zeck(x):
    res = []
    for i in range(len(fib)-1, -1, -1):
        if fib[i] <= x:
            x -= fib[i]
            res.append(fib[i])
        if x == 0:
            break
    return res

t = int(input())
for _ in range(t):
    x = int(input())
    print(*zeck(x)[::-1])