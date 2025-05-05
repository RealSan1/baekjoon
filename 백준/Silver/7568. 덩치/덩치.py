import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

result = []
for i in range(N):
    A = list(filter(lambda x: x!= arr[i], arr))
    rank = len(list(filter(lambda x : arr[i][0] < x[0] and arr[i][1] < x[1], A)))+1
    result.append(rank)

print(*result)