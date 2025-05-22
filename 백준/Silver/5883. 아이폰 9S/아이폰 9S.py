import sys
input = sys.stdin.readline

N = int(input())
arr = []
cut = set()
for _ in range(N):
    B = int(input())
    cut.add(B)
    arr.append(B)

T = 1
for i in cut:
    result = 1
    V = 1
    temp = []
    for j in arr:
        if i != j:
            temp.append(j)
    for k in range(len(temp)-1):
        if temp[k] == temp[k+1]:
            result += 1
            T = max(result, T)
        else:
            result = 1

print(T)