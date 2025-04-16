import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A = input().strip()
    
    if len(A) >= 6 and len(A) <= 9:
        print("yes")
    else:
        print("no")