import sys
input = sys.stdin.readline

N, C = map(str, input().split())
if C.count('?') != 0:
    C = C.replace('?', '9')
C = int(C)
A = int(input())
if C >= A:
    print(C)
else:
    print(-1)