import sys
input = sys.stdin.readline

N = int(input())
temp = []
for _ in range(N):
    temp.append(input().strip())

arr = []
K = 1

while True:
    if len(arr) == N:
        break

    for i in temp:
        i = i[-1 * K:]
        if i in arr:
            arr = []
            break
        else:
            arr.append(i)
    K += 1

print(K-1)