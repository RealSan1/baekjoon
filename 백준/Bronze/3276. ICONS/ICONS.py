import sys
input = sys.stdin.readline

N = int(input())
A, B = 1, 1
while True:
    if A * B >= N:
        break
    B += 1
    if A * B >= N:
        break
    A += 1
    if A * B >= N:
        break

print(A, B)