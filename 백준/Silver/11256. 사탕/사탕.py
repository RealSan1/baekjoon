T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    arr = []
    result = 0

    for i in range(N):
        R, C = map(int, input().split())
        arr.append(R*C)
    arr.sort(reverse=True)

    for i in arr:
        J -= i
        result += 1
        if J <= 0:
            print(result)
            break

