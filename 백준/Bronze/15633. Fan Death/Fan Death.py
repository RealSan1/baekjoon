N = int(input())
arr = []
for i in range(N, 0, -1):
    if N % i == 0:
        arr.append(i)

print((sum(arr) * 5) - 24)