import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    try:
        s, t = input().split()
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        if i == len(s):
            print("Yes")
        else:
            print("No")
    except:
        break