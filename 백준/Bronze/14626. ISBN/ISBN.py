import sys
input = sys.stdin.readline

ISBN = input().strip()

num = 0
for i, j in enumerate(ISBN):
    if j.isalnum():
        if i % 2 == 0:
            num += int(j) * 1
        else:
            num += int(j) * 3

check = ISBN.index('*')
if check % 2 == 0:
    check = 1
else:
    check = 3

for i in range(0, 10):
    if ((i * check) + num) % 10 == 0:
        print(i)
        break
