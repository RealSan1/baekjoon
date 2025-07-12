import sys
input = sys.stdin.readline

N = int(input())
for n in range(N):
    num = list(input().strip())
    res = ''
    for i in num:
        temp = ord(i) + 1
        if temp >= 91:
            temp = 65
        res += chr(temp)

    print(f"String #{n+1}")
    print(res)
    print()