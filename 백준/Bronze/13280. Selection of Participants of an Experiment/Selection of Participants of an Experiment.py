import sys
input = sys.stdin.readline
  
while True:
    N = int(input())
    if N == 0:
        break
    arr = list(map(int, input().split()))
    arr.sort()
    res = sys.maxsize
    for i in range(len(arr)-1):
        num = arr[i+1] - arr[i]
        res = min(res, num)
    print(res)