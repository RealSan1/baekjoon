import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rank = {}
final = {}
for i in range(N):
    A = int(input())
    if A in rank.values():
        rank[i+1] = A
        for key, value in rank.items():
            if value >= A and key != i+1:
                rank.update({key: value+1})
    else:
        rank[i+1] = A

rank = sorted(rank.items(), key=lambda x: x[1])[:M]

for i, j in rank[::-1]:
    A = int(input())
    if A in final.values():
        final[i] = A
        for key, value in final.items():
            if value >= A and key != i:
                final.update({key: value+1})
    else:
        final[i] = A

for i, j in sorted(final.items(), key=lambda x: x[1])[:3]:
    print(i)