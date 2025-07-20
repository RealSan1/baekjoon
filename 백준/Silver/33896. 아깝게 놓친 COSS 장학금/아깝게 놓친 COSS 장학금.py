import sys
input = sys.stdin.readline
  
N = int(input())
arr = {}
for _ in range(N):
    num = list(input().split())
    name, score, risk, cost = num[0], int(num[1]), int(num[2]), int(num[3])
    res = (score ** 3) // (cost * (risk + 1))
    arr[name] = [res, cost]

arr = sorted(arr.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
print(arr[1][0])