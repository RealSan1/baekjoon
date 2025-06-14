import sys
input = sys.stdin.readline

K = int(input())
S = input().strip()
count = 0
num = S[0]
for i in S:
    if count == K:
        num += i
        count = 0
    count += 1
print(num)
    