import sys, math
input = sys.stdin.readline

info = {'F': 0, 'D0': 100, 'D+': 150, 'C0': 200, 'C+': 250, 
        'B0': 300, 'B+': 350, 'A0': 400, 'A+': 450}

res = 0
num = 0
N, X = map(float, input().split())
N, X = int(N), int(round(X*100))
for _ in range(N-1):
    C, G = map(str, input().split())
    num += int(C)
    res += info[G] * int(C) # 과목 성적

C = int(input())
num += C

Bool = True
for key, value in info.items():
    if int(int(((value * C) + res)) / num) > X:
        print(key)
        Bool = False
        break

if Bool:
    print("impossible")