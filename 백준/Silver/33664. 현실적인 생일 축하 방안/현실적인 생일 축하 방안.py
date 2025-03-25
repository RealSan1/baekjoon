import sys
input = sys.stdin.readline

arr = {}
B, N, M = map(int, input().split())
for _ in range(N):
    item = input().split()
    arr[item[0]] = int(item[1])

price = 0
for _ in range(M):
    item = input().strip()
    price += arr[item]

if B >= price:
    print('acceptable')
else:
    print('unacceptable')