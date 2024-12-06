N = int(input())
i = 2
arr = []
while True:
    if N % i == 0:
        arr.append(i)
        N = N//i
        i = 2
    else:
        i += 1
    if N == 1:
        break

arr.sort()

for i in arr:
    print(i)