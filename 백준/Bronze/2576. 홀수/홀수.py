var = 0
arr = []
for i in range(7):
    N = int(input())
    if N % 2 != 0 :
        var += N
        arr.append(N)

if len(arr) == 0:
    print(-1)
else:
    print(var)
    print(min(arr))