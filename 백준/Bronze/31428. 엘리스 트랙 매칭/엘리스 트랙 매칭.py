import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(str, input().strip().split()))
C = input().strip()

print(arr.count(C))