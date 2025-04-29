import sys
input = sys.stdin.readline

N = int(input())
C = []
for _ in range(N):
    C.append(int(input()))
C.sort(reverse=True)

count, result = 0, 0
for i in C:
    result += i
    count += 1
    if count == 3:
        result -=i
        count = 0

print(result)