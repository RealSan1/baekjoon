import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
arr = {}
for n in range(N):
    A = list(map(str, input().split()))
    arr[A[0]] = int(A[1])

num = 0
for k in range(K):
    B = input()
    num += arr[B]
    arr.pop(B)
    M -= 1

count = list(arr.values())
count.sort()
MIN = MAX = num

for i in range(M):
    MIN += count[i]

for i in range(M):
    MAX += count[-i - 1]

print(MIN, MAX)