import sys
input = lambda: sys.stdin.readline().rstrip()

num = list(map(int, input().split()))
num.sort()

print(max(num[0] + num[1] * num[2], num[0] * num[1] + num[2]))