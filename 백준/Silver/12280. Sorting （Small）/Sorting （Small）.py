import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    Alex, Bob = [], []
    S = list(map(int, input().split()))
    for i in S:
        if i % 2 == 0:
            Bob.append(i)
        else:
            Alex.append(i)
    Bob.sort(reverse=True)
    Alex.sort()

    res = []
    B, A = 0, 0
    for i in S:
        if i % 2 == 0:
            res.append(Bob[B])
            B += 1
        else:
            res.append(Alex[A])
            A += 1

    print(f"Case #{_+1}:", *res)