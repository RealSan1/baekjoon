import sys
input = sys.stdin.readline

T = int(input())
arr = []
result = -1
for _ in range(T):
    arr.append(int(input()))

arr.sort()

while len(arr) >= 3:
    A = arr.pop()
    B = arr.pop()
    C = arr.pop()
    if B + C > A:
        result = A + B + C
        break
    arr.append(C)
    arr.append(B)

print(result)