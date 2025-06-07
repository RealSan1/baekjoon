import sys
input = sys.stdin.readline

N = int(input())
arr = []
prices = []
result, num = 0, 0
for _ in range(N):
    A, B = map(int, input().split())
    prices.append(A)
    arr.append([A, B])

for price in prices: #물건가격
    count = 0
    for j in range(len(arr)):
        if arr[j][0] >= price:
            if price - arr[j][1] > 0:
                count += price - arr[j][1]

    if count > num or (count == num and price < result):
        result = price
        num = count

print(result)
