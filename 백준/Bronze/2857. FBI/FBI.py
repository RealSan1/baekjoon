import sys
input = sys.stdin.readline

arr = []
for i in range(5):
    name = input()
    if 'FBI' in name:
        arr.append(i+1)

if arr == []:
    print('HE GOT AWAY!')
else:
    print(*arr)