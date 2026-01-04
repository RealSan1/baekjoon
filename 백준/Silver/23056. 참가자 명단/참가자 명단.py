import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
Blue = {}
Red = {}
while True:
    A = list(map(str, input().split()))
    if A[0] == '0' and A[1] == '0':
        break
    num = int(A[0])
    if num % 2 == 0:
        if num in Red :
            if len(Red[num]) < M:
                Red[num] += [A[1]]
            else:
                continue
        else:
            Red[num] = [A[1]]
    else:
        if num in Blue:
            if len(Blue[num]) < M:
                Blue[num] += [A[1]]
            else:
                continue
        else:
            Blue[num] = [A[1]]

for cls in sorted(Blue.keys()):
    students = sorted(Blue[cls], key=lambda x: (len(x), x))
    for i in students:
        print(cls, i)

for cls in sorted(Red.keys()):
    students = sorted(Red[cls], key=lambda x: (len(x), x))
    for i in students:
        print(cls, i)
