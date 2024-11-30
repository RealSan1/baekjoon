N, K = map(int, input().split())
arr = []
num = 0
for i in range(N):
    arr.append(int(input()))

for calculator in reversed(arr):
    if K == 0:
        break 
    if K >= calculator:
        num += K // calculator
        K %= calculator

print(num)