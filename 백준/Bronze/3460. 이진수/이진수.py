import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = int(input())
    res = []
    for i, j in enumerate(bin(A)[2:][::-1]):
        if j == '1':
            res.append(i)
    print(*res)