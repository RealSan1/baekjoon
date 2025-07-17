import sys
input = sys.stdin.readline
  
N = int(input())
res = 0
for _ in range(N):
    num = input().strip().lower()
    
    temp = 0
    temp += num.count('pink')
    temp += num.count('rose')
    if temp > 0:
        res += 1

if res != 0:
    print(res)
else:
    print("I must watch Star Wars with my daughter")