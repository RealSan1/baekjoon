import sys
input = sys.stdin.readline

S = input().strip()
Bool = False
arr, result = '', ''

for i in S:
    if i == '<':
        result += arr[::-1]
        arr = ''
        Bool = True
        result += i
    elif i == '>':
        Bool = False
        result += i
    elif Bool:
        result += i
    elif not Bool:
        if i == ' ':
            result += arr[::-1] + ' '
            arr = ''
        else:
            arr += i

result += arr[::-1]
print(result)