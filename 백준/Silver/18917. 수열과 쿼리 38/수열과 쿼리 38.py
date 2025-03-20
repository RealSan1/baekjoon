import sys
input = sys.stdin.readline

M = int(input())
HAP = 0
XOR = 0
for _ in range(M):
    keyword = list(map(int, input().split()))
    if len(keyword) == 2:
        if keyword[0] == 1:
            HAP += keyword[1]
            XOR ^= keyword[1]

        elif keyword[0] == 2:
            HAP -= keyword[1]
            XOR ^= keyword[1]
    else:
        if keyword[0] == 3:
            print(HAP)

        elif keyword[0] == 4:
            print(XOR)
