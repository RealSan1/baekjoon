var = 0
N = int(input())
L = list(map(int, input().split()))
L.sort()
arr = []
for i in range(N):
    var += L[i]
    arr.append(var)

print(sum(arr))