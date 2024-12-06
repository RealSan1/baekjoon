arr = []
for i in range(9):
    A = int(input())
    arr.append(A)

arr.sort()

for i in range(9):
    for j in range(9):
        if 100 == sum(arr) - arr[j] - arr[i]:
            a = arr[j]
            b = arr[i]

arr.remove(a)
arr.remove(b)

for i in arr:
    print(i)