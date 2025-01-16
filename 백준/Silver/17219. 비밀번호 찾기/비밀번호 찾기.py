N, M = map(int, input().split())
save = dict()
for _ in range(N):
    site, password = map(str, input().split())
    save[site] = password

for _ in range(M):
    site = input()
    print(save.get(site))