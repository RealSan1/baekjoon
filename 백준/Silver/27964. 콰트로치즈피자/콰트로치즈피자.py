import sys
input = sys.stdin.readline

T = int(input())
word = list(map(str, input().split()))
arr = []
for i in word:
    if i[-6:] == 'Cheese':
        if i in arr:
            continue
        else:
            arr.append(i)

if len(arr) >= 4:
    print('yummy')
else:
    print('sad')