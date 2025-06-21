import sys
input = sys.stdin.readline

A, B = map(int, input().split())
arr = {'0' : 0, '1' : 0, '2': 0, '3': 0, '3': 0, '4': 0,
       '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in range(A, B+1):
    i = str(i)
    for j in i:
        if j in arr:
            arr[j] += 1

print(*arr.values())
