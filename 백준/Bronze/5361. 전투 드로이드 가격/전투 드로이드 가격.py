import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    num = list(map(int, input().split()))
    res = 0
    res += 350.34 * num[0]
    res += 230.90 * num[1]
    res += 190.55 * num[2]
    res += 125.30 * num[3]
    res += 180.90 * num[4]
    print(f"${res:.2f}")