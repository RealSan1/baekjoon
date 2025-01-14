N, M = map(int, input().split())
arr = []
result = 0
for _ in range(N):
    A = input()
    arr.append(A)

for _ in range(M):
    A = input()
    if A in arr:
        result +=1

print(result)