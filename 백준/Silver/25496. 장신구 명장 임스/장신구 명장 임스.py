P, N = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
var = 0
for i in range(N):
    if P < 200:
        P += L[i]
        var += 1
    else:
        break

print(var)