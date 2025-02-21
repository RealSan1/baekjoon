import sys
input = sys.stdin.readline

L, P = map(int, input().split())
arr = list(map(int, input().split())) 
A = L * P
print(arr[0] - A, arr[1] - A, arr[2] - A, arr[3] - A, arr[4] - A)