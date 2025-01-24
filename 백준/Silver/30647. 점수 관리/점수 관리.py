import json

T = int(input())
lines = []
for _ in range(T):
    lines.append(input().strip())
json_data = json.loads("".join(lines))


temp = [[entry['name'], entry['score'], entry['isHidden']] for entry in json_data]

temp.sort(key=lambda x: (-x[1], x[0]))


result = []
current_rank = 1
current_score = None

for i, (name, score, isHidden) in enumerate(temp):
    if current_score != score:
        current_rank = i + 1
        current_score = score
    
    if isHidden == 0:
        result.append([current_rank, name, score])


for r in result:
    print(*r)
