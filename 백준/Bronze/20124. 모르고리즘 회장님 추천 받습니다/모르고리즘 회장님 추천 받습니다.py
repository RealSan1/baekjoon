N = int(input())
info = {'A' : 0} #기본 값
for _ in range(N):
    A = input().split()
    if max(info.values()) <= int(A[1]):
        info[A[0]] = int(A[1])

info.pop('A')

sort = sorted(info.items(), key=lambda x: (-x[1], x[0]))
print(sort[0][0])