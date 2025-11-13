import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
std = list(map(int, input().split()))
A = B = C = 0
for i in std:
    if i == 1:
        A += 1
    elif i == -1:
        B += 1
    elif i == 0:
        C += 1

if C >= N / 2:
    print('INVALID')
    exit()

if A > B:
    print('APPROVED')

elif B > A:
    print('REJECTED')

elif A == B:
    print('REJECTED')