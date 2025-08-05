import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
res = sum(num)
num = list(map(int, input().split()))
res = max(res, sum(num))
print(res)