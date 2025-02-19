import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
for i in range(N):
    A = input().strip()
    count = 0
    for t in A:
        if t.isdigit():
            count += int(t)
    arr[i] = [A, len(A), count]

sort = sorted(arr, key=lambda x: (x[1], x[2], x[0]))

for i in sort:
    print(i[0])