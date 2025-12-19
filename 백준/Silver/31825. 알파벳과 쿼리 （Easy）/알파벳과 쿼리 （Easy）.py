import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
num = list(input())
def alpha(num):
    arr = []
    V = num[0]
    for i in num[1:]:
        if V[-1] != i:
            arr.append(V)
            V = i
        else:
            V += i

    arr.append(V)
    return arr

for _ in range(Q):
    S, L, R = map(int, input().split())
    if S == 1:
        print(len(alpha(num[L-1:R])))
    else:
        for i in range(L-1, R):
            if ord(num[i]) + 1 == 91:
                num[i] = 'A'
            else:
                num[i] = chr(ord(num[i]) + 1)