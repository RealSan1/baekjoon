import sys
input = sys.stdin.readline

N, M = map(int, input().split())
title = []
for _ in range(N):
    A = input().strip().split()
    title.append([A[0], int(A[1])])

for _ in range(M):
    power = int(input())
    start = 0
    end = len(title) - 1
    while start <= end:
        mid = (start + end) // 2
        if power > title[mid][1]:
            start = mid + 1
        else:
            end = mid - 1
    mid = start
    print(title[mid][0])