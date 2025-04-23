import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
result = 0
temp = L
cow = []
for _ in range(N):
    cow.append(int(input()))
cow.sort()

for i in cow:
    if temp >= i:
        result +=1
        temp += K

print(result)