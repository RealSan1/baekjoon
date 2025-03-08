import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

pre = sum(arr[:X])
max_sum = pre
count = 1

for i in range(X,N):
    A1 = arr[i]
    A2 = arr[i-X]
    pre += arr[i] - arr[i-X]
    if pre > max_sum:
        max_sum = pre
        count = 1
    elif pre == max_sum:
        count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)