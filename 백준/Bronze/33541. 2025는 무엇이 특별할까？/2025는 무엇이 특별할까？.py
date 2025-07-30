import sys
input = sys.stdin.readline

N = int(input())
Bool = False
for i in range(N+1, 10000):
    A = i // 100
    B = i % 100
    if (A +B) ** 2 == i:
        Bool = True
        break

if Bool:
    print(i)
else:
    print(-1)