import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = set()
for V in range(R):
    A = input().strip()
    for i in A[1:]:
        if i.isdigit():
            arr.add((i, A.index(i)))

result = []
pre = 0
rank = 1
# print(sorted(arr, key=lambda x : -x[1]))
for i, j in sorted(arr, key=lambda x : -x[1]):
    if pre == j:
        rank -= 1
        result.append([i, rank])
    else:
        result.append([i, rank])
    
    rank += 1
    pre = j
# print(result)

for i, j in sorted(result, key=lambda x: x[0]):
    print(j)