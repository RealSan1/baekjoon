N = int(input())
L = list(map(int, input().split()))
result = 0
j = 1
for i in range(N):
    if L[i] == 1:
        result += j
        j += 1
    else:
        j = 1

print(result)