import sys
input = lambda: sys.stdin.readline().rstrip()

fib = [1, 2]
while fib[-1] <= 25000:
    fib.append(fib[-1] + fib[-2])

def zeck(x):
    bits = [0] * len(fib)
    for i in range(len(fib)-1, -1, -1):
        if fib[i] <= x:
            bits[i] = 1
            x -= fib[i]
        if x == 0:
            break
    return bits

def value(bits):
    s = 0
    for i in range(len(bits)):
        if bits[i] == 1:
            s += fib[i]
    return s

t = int(input())
for _ in range(t):
    x = int(input())
    bits = zeck(x)
    bits = bits[1:] + [0]
    print(value(bits))
