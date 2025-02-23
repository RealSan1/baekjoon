import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x = int(input())
    if x == 0:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)
    else:
        heapq.heappush(arr, x)
    