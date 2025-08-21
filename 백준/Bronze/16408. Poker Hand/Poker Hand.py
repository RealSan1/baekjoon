import sys
input = lambda: sys.stdin.readline().rstrip()

card = list(map(str, input().split()))
res = {}
for i in card:
    if i[0] in res:
        res[i[0]] += 1
    else:
        res[i[0]] = 1

print(max(res.values()))