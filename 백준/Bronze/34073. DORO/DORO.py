import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().split()))
for i in arr:
    res = i + "DORO"
    print(res, end=' ')