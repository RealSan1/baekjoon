N, K = map(int, input().split())
arr = []
temp = None
rank = []
for i in range(N):
    L = list(map(int, input().split()))
    arr.append(L)

arr.sort(key = lambda x :(x[1], x[2], x[3]), reverse=True) # 순위 졍렬

for row in arr:
    score = (row[1], row[2], row[3])
    if temp == score:
        rank[-1].append(row[0])
    else:
        rank.append([row[0]])
        temp = score

for i, group in enumerate(rank):
    if K in group:
        print(i+1)
        break