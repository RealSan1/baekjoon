import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    j, p = map(int, input().split())
    try:
        result = j/p
    except:
        result = 0.0

    arr.append([i+1, j, p, result])

V = sorted(arr, key=lambda x: -x[3])[:3]
price = 0
for i,j,a,b in V:
    price += a

print(price)
for i,j,a,b in V:
    print(i)