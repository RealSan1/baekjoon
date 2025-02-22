import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    for i in list(map(int, input().strip().split())):
        if len(arr) < N:
            heapq.heappush(arr, i)
        else:
            heapq.heappushpop(arr, i)

print(arr[0])