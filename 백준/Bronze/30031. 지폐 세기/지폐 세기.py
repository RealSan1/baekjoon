N = int(input())
temp = 0
for _ in range(N):
    T = list(map(int, input().split()))
    if T[0] == 136:
        temp += 1000
    elif T[0] == 142:
        temp += 5000
    elif T[0] == 148:
        temp += 10000
    elif T[0] == 154:
        temp += 50000
print(temp)