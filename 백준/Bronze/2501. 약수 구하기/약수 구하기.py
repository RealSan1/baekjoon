N, K = map(int, input().split())
arr = []
for i in range(N, 0, -1):
    if N % i == 0:
        arr.append(i)
arr.reverse()

try:
    print(arr[K-1])
except IndexError:
    print(0)