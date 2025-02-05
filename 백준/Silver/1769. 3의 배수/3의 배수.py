import sys
input = sys.stdin.readline

X = input().strip()

temp = 0
result = 0
while True:
    if len(X) == 1:
        break

    for i in X:
        temp += int(i)

    X = str(temp)
    temp = 0
    result += 1

print(result)

if int(X) % 3 == 0:
    print('YES')
else:
    print('NO')