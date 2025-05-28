import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input()
    num = input().strip()    
    num = ''.join(sorted(num, reverse=True))
    A = int(num[:-1])
    B = int(num[-1])
    print(A+B)
