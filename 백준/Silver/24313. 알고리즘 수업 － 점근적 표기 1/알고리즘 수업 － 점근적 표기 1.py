A1, A0 = map(int, input().split())
C = int(input())
N = int(input())

if (A1*N + A0) <= C*N and A1 <= C:
    print(1)
else:
    print(0)
