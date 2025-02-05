import sys
input = sys.stdin.readline

N = int(input())

arr = []
result = ""
for _ in range(N):
    S, I, D = map(str, input().split())
    I = int(I)
    D = int(D)
    cut = S.upper()[D-1]
    arr.append([I, cut])
arr.sort(key=lambda x: x[0])

for i, j in arr:
    result += j

print(result)