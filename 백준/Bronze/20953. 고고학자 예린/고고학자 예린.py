import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    num = ((a + b)**2 * (a + b - 1)) / 2
    print(int(num))