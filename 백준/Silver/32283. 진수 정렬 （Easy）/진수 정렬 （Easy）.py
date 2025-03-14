import sys
input = sys.stdin.readline

N = int(input())
find = input().strip()
arr = [0] * 2**N
for i in range(2**N):
    arr[i] = (bin(i)[2:].zfill(N))

arr = sorted(arr, key = lambda x: (x.count('1'), x[::-1]))

print(arr.index(find))