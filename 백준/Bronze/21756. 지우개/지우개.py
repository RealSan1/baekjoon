import sys
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(1, N+1)]

while True:
    if arr.count(0) == N-1:
        break
    temp = []
    for i, j in enumerate(arr):
        if i % 2 != 0 and j != 0:
            temp.append(j)
    arr = [0] * N
    for i in range(len(temp)):
        arr[i] = temp[i]

print(arr[0])