import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()
num = 'UAPC'
for i in N:
    num = num.replace(i, '')

print(num)