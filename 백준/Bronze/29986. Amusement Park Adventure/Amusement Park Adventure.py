import sys
input = sys.stdin.readline

A, B = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in arr:
    if B >= i:
        result += 1

print(result)