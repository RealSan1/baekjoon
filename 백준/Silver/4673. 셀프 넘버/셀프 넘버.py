import sys
input = sys.stdin.readline

A = 0
result = set()
count = set(i for i in range(1, 10000))
while True:
    if A == 10000:
        break
    A += 1
    A = str(A)
    num = int(A)
    for i in A:
        num += int(i)
    A = int(A)
    if num < 10000:
        result.add(num)

result = count - result
for i in sorted(result):
    print(i)