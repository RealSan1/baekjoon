N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
for i in range(N):
    if L >= arr[i]:
        L += 1
print(L)