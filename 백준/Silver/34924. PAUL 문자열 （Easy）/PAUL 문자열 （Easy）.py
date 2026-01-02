import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num = input()
arr = []
Bool = True

arr.append(num.find('P'))
arr.append(num.find('A'))
arr.append(num.find('U'))
arr.append(num.find('L'))

V = arr[0]
for i in arr[1:]:
    if i < V:
        Bool = False
    V = i

if arr[0] % 2 != 0:
    Bool = False

if (N - arr[-1] - 1) % 2 != 0:
    Bool = False

V = arr[0]
for i in arr[1:]:
    if (i - V) % 2 == 0 and i - V != 1:
        Bool = False
    V = i

if Bool:
    print("YES")
else:
    print("NO")