import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = 1
if m <= n:
    result = 0

else:
    for i in range(n, 0, -1):
        result *= i
        result %= m
        if result == 0:
            break

print(result)