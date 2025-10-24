import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = N * (N**2 + 1) / 2
arr = []
z = []
for i in range(N):
    T = list(map(int, input().split()))
    z += set(T)
    arr.append(T)

if len(z) != N ** 2: # 1번 조건
    print('FALSE')
    exit()

for i in range(N): # 행의 합
    if res != sum(arr[i]):
        print('FALSE')
        exit()

for i in range(N): # 열의 합
    t = 0
    for j in range(N):
        t += arr[j][i]
    if t != res:
        print('FALSE')
        exit()

left = 0
for i in range(N): # 대각선 왼쪽 합
    left += arr[i][i]

right = 0
for i in range(N): # 대각선 오른쪽 합
    right += arr[N-i-1][i]

if left != right != res:
    print('FALSE')
    exit()

print('TRUE')
