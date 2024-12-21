N, M = map(int, input().split())
듣도 = set()
보도 = set()
for i in range(N):
    듣도.add(input())

for j in range(M):
    보도.add(input())

듣보잡 = 듣도 & 보도


print(len(듣보잡))
for i in sorted(듣보잡):
    print(i)