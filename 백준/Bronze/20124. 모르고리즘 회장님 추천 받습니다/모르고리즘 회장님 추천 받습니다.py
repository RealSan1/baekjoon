N = int(input())
info = {}
for _ in range(N):
    A = input().split()
    info[A[0]] = int(A[1])

sort = sorted(info.items(), key=lambda x: (-x[1], x[0]))
print(sort[0][0])