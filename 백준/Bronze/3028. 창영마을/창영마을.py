import sys
input = lambda: sys.stdin.readline().rstrip()

num = input()
CUP = [1, 0, 0]
for i in num:
    if i == "A":
        CUP[0], CUP[1] = CUP[1], CUP[0]
    elif i == "B":
        CUP[1], CUP[2] = CUP[2], CUP[1]
    elif i == "C":
        CUP[0], CUP[2] = CUP[2], CUP[0]

print(CUP.index(1) + 1)