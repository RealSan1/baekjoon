T = int(input())
C = int(input())
arr = []
for _ in range(C):
    A = int(input())
    arr.append(A)

arr.sort()
result = 0
for i in arr:
    if T - i >= 0:
        T -= i
        result += 1
    else:
        break

print(result)
