N = int(input())
arr = []
for _ in range(N):
    Info = list(map(str, input().split()))
    year = int(Info[3])
    month = int(Info[2])
    day = int(Info[1])
    arr.append((Info[0], year, month, day))

print(max(arr, key=lambda x: (x[1], x[2], x[3]))[0])
print(min(arr, key=lambda x: (x[1], x[2], x[3]))[0])