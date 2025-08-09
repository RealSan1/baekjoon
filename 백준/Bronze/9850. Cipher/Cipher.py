import sys
input = lambda: sys.stdin.readline().rstrip()

def dec(num, shift):
    result = ''
    for char in num:
        if char.isalpha():
            char_idx = ord(char) - ord('A')
            plain_idx = (char_idx - shift) % 26
            result += chr(plain_idx + ord('A'))
        else:
            result += char
    return result

num = input()

for p in range(26):
    res = dec(num, p)
    if "CHIPMUNKS" in res and "LIVE" in res:
        print(res)
        break