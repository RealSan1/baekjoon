import sys
input = sys.stdin.readline

N, B, H, W = map(int, input().split())
result = sys.maxsize

for _ in range(H):
    price = int(input())
    room = list(map(int, input().split()))
    if N <= max(room) and price * N <= B:
        temp = price * N        
        result = min(result, temp)

if result == sys.maxsize:
    print('stay home')
else:
    print(result)