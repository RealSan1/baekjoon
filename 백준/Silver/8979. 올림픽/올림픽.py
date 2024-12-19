N, K = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)


rank = [0] * (N + 1) 
current_rank = 1      
prev_score = None     

for i, row in enumerate(arr):
    score = (row[1], row[2], row[3])
    if score == prev_score:  
        rank[row[0]] = current_rank
    else:  
        current_rank = i + 1
        rank[row[0]] = current_rank
    prev_score = score

print(rank[K])