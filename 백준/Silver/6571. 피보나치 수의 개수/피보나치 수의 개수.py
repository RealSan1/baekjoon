import sys
input = sys.stdin.readline

arr = [0] * 100001
arr[0], arr[1] = 1, 2
for i in range(2, len(arr)):
    arr[i] = arr[i-1] + arr[i-2]

while True:

    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    result = 0

    for i in arr:
        if i > B:
            break

        if i >= A:
            result += 1
            

    print(result)