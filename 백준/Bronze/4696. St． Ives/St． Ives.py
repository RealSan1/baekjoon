import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    N = float(input())
    if N == 0:
        break

    res = 0
    for i in range(5):
        res += N ** i

    print(f"{res:.2f}")