N, M = map(int, input().split())
temp = [i + 1 for i in range(1, N)]
arr = []
for i in range(len(temp)):
    if temp[i] % (i+2) == 0:
        for j in range(len(temp)):
            if temp[j] % (i+2) == 0:
                if temp[j] not in arr:
                    arr.append(temp[j])

print(arr[M-1])