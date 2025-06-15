import sys
input = sys.stdin.readline

n, p = map(int, input().split())
for i in range(n):
    A, B = map(str, input().split())
    
if p > n // 3 and p <= n - (n + 1) // 3:
    print("YES")
else:
    print("NO")
