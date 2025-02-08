import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
hap = sum(arr) ** 2
for i in arr:
    hap -= i*i

print(hap//2)
