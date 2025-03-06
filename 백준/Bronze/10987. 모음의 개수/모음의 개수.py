import sys
input = sys.stdin.readline

moum = ['a','e','i','o','u']

word = input()
result = 0
for i in word:
    if i in moum:
        result += 1

print(result)