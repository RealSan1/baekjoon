from sys import stdin

N, A = map(int,stdin.readline().split())

arr = list(map(int,stdin.readline().split()))
arr.sort()

print(arr[A-1])