import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = []
for i in range(N):
    A, B = map(int, input().split())
    arr.append([i+1, A, B])

# print(arr)
arr = sorted(arr, key=lambda x : -x[1])[:K]
# print(arr)
arr = sorted(arr, key=lambda x : -x[2])

print(arr[0][0])