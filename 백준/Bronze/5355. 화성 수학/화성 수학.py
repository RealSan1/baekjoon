T = int(input())
for i in range(T):
    N = list(input().split())
    var = float(N[0])
    N = N[1:]
    for j in N:
        if j == '@':
            var *= 3
        elif j == '%':
            var +=  5
        elif j == '#':
            var -= 7
    print(f"{var:.2f}")
