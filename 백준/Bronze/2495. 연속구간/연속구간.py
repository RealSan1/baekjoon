import sys
input = sys.stdin.readline

for _ in range(3):
    N = input().strip()
    V = N[0]
    res = 1
    arr = []
    for i in N[1:]:
        if V == i:
            res += 1
        else:
            arr.append(res)
            res = 1
        V = i
    arr.append(res)
    print(max(arr))