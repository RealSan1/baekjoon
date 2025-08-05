import sys
input = sys.stdin.readline

num = input().strip()
if num[:2] == '0x':
    print(int(num, base=16))
elif num[0] == '0':
    print(int(num, base=8))
else:
    print(int(num))