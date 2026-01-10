import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for n in range(N):
    num = input()
    res = 0
    for i in range(len(num)):
        if len(num[i:i+3]) != 3:
            break

        if num[i:i+3] == "WOW":
            res += 1
    print(res)