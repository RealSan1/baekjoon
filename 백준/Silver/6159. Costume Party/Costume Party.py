N, S = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()

result = 0
left, right = 0, N - 1

while left < right:
    if arr[left] + arr[right] <= S:
        result += (right - left)
        left += 1
    else:
        right -= 1

print(result)