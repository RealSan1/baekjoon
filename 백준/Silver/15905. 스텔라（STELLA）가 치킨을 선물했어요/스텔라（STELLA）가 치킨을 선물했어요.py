import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    A, B = map(int, input().split())
    arr.append([A, B]) # 해결, 패널티

sort = sorted(arr, key=lambda x: (-x[0], x[1]))
five = sort[4]

result = 0
for i in sort:
    if five[0] == i[0] and five[1] < i[1]:
        result += 1

print(result)