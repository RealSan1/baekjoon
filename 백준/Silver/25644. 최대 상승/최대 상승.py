N = int(input())
arr = list(map(int, input().split()))
min_price = arr[0]
max_price = 0
for i in range(1, N):
    min_price = min(min_price, arr[i-1])

    max_price = max(max_price, arr[i] - min_price)

print(max_price)