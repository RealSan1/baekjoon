import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    H, M, S = map(int, input().split())
    arr.append([H,M,S])

for i in sorted(arr, key=lambda x: (x[0], x[1], x[2])):
    print(*i)
