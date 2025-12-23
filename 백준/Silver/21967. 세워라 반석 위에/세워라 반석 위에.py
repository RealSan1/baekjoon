import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_dq = deque()
min_dq = deque()

l = 0
res = 0

for r in range(N):
    while max_dq and max_dq[-1] < arr[r]:
        max_dq.pop()
    max_dq.append(arr[r])

    while min_dq and min_dq[-1] > arr[r]:
        min_dq.pop()
    min_dq.append(arr[r])

    while max_dq[0] - min_dq[0] > 2:
        if arr[l] == max_dq[0]:
            max_dq.popleft()
        if arr[l] == min_dq[0]:
            min_dq.popleft()
        l += 1

    res = max(res, r - l + 1)

print(res)
