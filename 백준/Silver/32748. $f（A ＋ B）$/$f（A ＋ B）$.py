import sys
input = sys.stdin.readline

def solve(num):
    num = list(map(int, str(num)))
    temp = ''
    for i in num:
        temp += str(arr.index(i))

    temp = int(temp)
    return temp

result = 0
arr = list(map(int, input().split()))
A, B = map(int, input().split())

result += solve(A)
result += solve(B)

num = list(map(int, str(result)))
temp = ''
for i in num:
    temp += str(arr[i])

print(temp)