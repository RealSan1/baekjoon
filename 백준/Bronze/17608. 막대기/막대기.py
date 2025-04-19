import sys
input = sys.stdin.readline

N = int(input())
result = 1
arr = []
for _ in range(N-1):
    A = int(input())
    arr.append(A)

last = int(input())
for i in arr[::-1]:
    if i > last:
        result += 1
        last = i

print(result)