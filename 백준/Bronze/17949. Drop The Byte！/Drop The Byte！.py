import sys
input = sys.stdin.readline

PASSWORD = input().strip()
N = int(input())
JINSU = map(str, input().split())
split = []
result = []
for i in JINSU:
    if i == 'char':
        split.append(2)
    elif i == 'int':
        split.append(8)
    elif i == 'long_long':
        split.append(16)

temp = 0
for i in split:
    i += temp
    result.append(int(PASSWORD[temp:i], base=16))
    temp = i

print(*result)