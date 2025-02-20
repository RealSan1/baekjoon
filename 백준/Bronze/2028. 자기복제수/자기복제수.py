import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = input().strip()
    A1 = str(int(A) ** 2)
    if A1.endswith(A):
        print('YES')
    else:
        print('NO')