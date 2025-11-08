import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(sum(arr[:N//2]), sum(arr[N//2:]))