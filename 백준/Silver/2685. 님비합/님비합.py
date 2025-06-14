import sys
input = sys.stdin.readline

def to_base(N, B):
    if N == 0:
        return [0]
    res = []
    while N:
        N, r = divmod(N, B)
        res.append(r)
    return res

def NimSum(B, X, Y):
    if len(X) < len(Y):
        X, Y = Y, X
    for i in range(len(Y)):
        X[i] = (X[i] + Y[i]) % B
    res, b = 0, 1
    for digit in X:
        res += digit * b
        b *= B
    return res

T = int(input())
for _ in range(T):
    B, X, Y = map(int, input().split())
    X = to_base(X, B)
    Y = to_base(Y, B)
    print(NimSum(B, X, Y))
