import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
han_id, han_mid = input().split()
han_mid = int(han_mid)

students = []

for _ in range(N - 1):
    sid, smid = input().split()
    smid = int(smid)
    if sid[:4] == '2024':
        lost = X - smid
        final = max(Y - lost, 0)
        total = smid + final
        students.append(total)

def APlus(han_final):
    han_total = han_mid + han_final
    scores = students + [han_total]
    scores.sort(reverse=True)
    
    ranks = {}
    for i, score in enumerate(scores):
        if score not in ranks:
            ranks[score] = i + 1
    return ranks[han_total] <= M

left, right = 0, Y
answer = -1

while left <= right:
    mid = (left + right) // 2
    if APlus(mid):
        answer = mid
        right = mid - 1  
    else:
        left = mid + 1

if answer != -1:
    print("YES")
    print(answer)
else:
    print("NO")
