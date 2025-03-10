import sys
input = sys.stdin.readline

A = input().strip()
N = int(input())
result = 0
for _ in range(N):
    ring = input().strip()
    for i in range(len(ring)):
        ring = ring[1:] + ring[0]
        if A in ring:
            result += 1
            break

print(result)