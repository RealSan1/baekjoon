import sys
input = lambda: sys.stdin.readline().rstrip()

def Zeller(y, m):
    if m < 3:
        m += 12
        y -= 1
    q = 13
    K = y % 100
    J = y // 100
    return (q + (13*(m+1))//5 + K + (K//4) + (J//4) + 5*J) % 7

N = int(input())
res = 0
for Y in range(2019, N+1):
    for M in range(1, 13):
        if Zeller(Y, M) == 6:
            res += 1
print(res)