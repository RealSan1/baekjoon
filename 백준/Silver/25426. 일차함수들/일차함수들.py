import sys
input = sys.stdin.readline

N = int(input())
Fx = 0
arr = []
for _ in range(N):
    A, B = map(int, input().split())
    arr.append([A,B])

for i, j in (sorted(arr, key=lambda x: (-x[0], x[1]))):
    Fx += i * N + j
    N -= 1

print(Fx)