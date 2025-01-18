N = int(input())
temp = {}
for i in range(N):
    A = input().split('.')
    if A[1] in temp:
        temp[A[1]] += 1
    else:
        temp[A[1]] = 1

temp = sorted(temp.items(), key=lambda x: x[0])

for i, j in temp:
    print(i, j)