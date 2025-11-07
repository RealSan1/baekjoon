import sys
input = lambda: sys.stdin.readline().rstrip()

num = 0
for i in range(4):
    n = int(input())
    num +=n
    
if num + 300 <= 1800:
    print('Yes')
else:
    print('No')