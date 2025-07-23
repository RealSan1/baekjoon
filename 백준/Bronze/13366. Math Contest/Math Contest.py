import sys
input = sys.stdin.readline
  
T = int(input())
for _ in range(T):
    A = list(map(int, input().strip()))
    
    if sum(A) % 9 == 0:
        print("YES")
    else:
        print("NO")