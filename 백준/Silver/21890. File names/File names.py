import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
res = 0
for _ in range(N):
    num = input()
    if num.count('.') == 1:
        filename, extension = num.split('.')
        if 1 <= len(filename) <= 8 and 1 <= len(extension) <= 3:
            res += 1

print(res)