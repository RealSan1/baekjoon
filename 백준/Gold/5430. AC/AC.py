import sys
input=lambda:sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    func = input() # 함수
    N = int(input())
    arr = input().strip('[]')
    if N == 0 :
        arr = []
    else:
        arr = arr.split(',')

    Error = False
    Re = False
    for i in func:
        if i == 'R':
            if not Re:
                Re = True
            else:
                Re = False
        elif i == 'D':
            try:
                if Re:
                    arr.pop()
                else:
                    arr.pop(0)
            except:
                Error = True
                break
    if Re:
        arr.reverse()

    if Error:
        print('error')
    else:
        print(f"[{','.join(arr)}]")
