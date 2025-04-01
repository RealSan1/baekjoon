import sys
input = sys.stdin.readline

while True:
    T = int(input())
    if T == 0:
        break
    
    page = set()
    arr = input().strip().split(',')
    for i in arr:
        if '-' in i:
            A, B = i.split('-')
            A = int(A)
            B = int(B)
            if A > B:
                continue
            else:
                for i in range(A, B+1):
                    if i <= T:
                        page.add(i)                    
        else:
            A = int(i)
            if A <= T:
                page.add(A)

    print(len(page))