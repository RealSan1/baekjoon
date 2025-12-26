import sys
input = sys.stdin.readline

N = int(input())

arr = [[0 for i in range(N)] for i in range(N)]


right = up = 0
left = down = N-1
num = 1

while True:
    try:

        for i in range(N):
            if arr[right][i] == 0:
                arr[right][i] = num                
                num += 1
        right += 1

        for i in range(N):
            if arr[i][down] == 0:
                arr[i][down] = num
                num += 1
        down -= 1

        for i in range(N-1, -1, -1):
            if arr[left][i] == 0:
                arr[left][i] = num
                num += 1
        left -= 1

        for i in range(N-1, -1, -1):
            if arr[i][up] == 0:
                arr[i][up] = num
                num += 1
        up += 1
    except:
        break

for i in arr:
    print(*i)
# print(arr)
