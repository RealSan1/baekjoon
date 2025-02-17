import sys
input = sys.stdin.readline

N = int(input())
n = 0
number = 0
while True:
    n += 1
    title = str(n)
    if '666' in title:
        number += 1
        if number == N: break

print(title)