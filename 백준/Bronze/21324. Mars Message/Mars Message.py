import sys
input = sys.stdin.readline

arr = []
Hex = []
N = int(input())
for _ in range(N):
    A = float(input())
    T = int(A//22.5)
    arr.append(hex(T))

temp = ''
for i, j in enumerate(arr):
    temp += j[2:]
    if i % 2 != 0:
        Hex.append(temp)
        temp = ''

result = ''
for i in Hex:
    result += (chr(int(i, base=16)))

print(result)