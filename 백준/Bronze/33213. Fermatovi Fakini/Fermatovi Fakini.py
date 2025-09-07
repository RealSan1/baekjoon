import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
odd = []
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) > len(odd):
    res = 2
    while True:
        if res not in even:
            print(res)
            break
        else:
            res += 2
else: 
    res = 1
    while True:
        if res not in odd:
            print(res)
            break
        else:
            res += 2