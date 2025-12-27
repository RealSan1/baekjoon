import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
num = arr[0]
Bool = True
for i in arr[1:]:
    if i <= num:
        Bool = False
        break
    num = i

if Bool:
    print(1)
else:
    print(0)