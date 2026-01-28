import sys
input = lambda: sys.stdin.readline().rstrip()

A = int(input())
B = int(input())
res = 0
for num in range(A, B+1):
    div = set()
    for i in range(1, num + 1):
        if num % i == 0:
            div.add(i)
            div.add(num // i)
    if len(div) == 4:
        res += 1

print(f"The number of RSA numbers between {A} and {B} is {res}")