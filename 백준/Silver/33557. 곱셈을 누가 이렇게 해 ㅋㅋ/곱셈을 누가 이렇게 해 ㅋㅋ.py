import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    num = int(A) * int(B)
    A = A[::-1]
    B = B[::-1]
    arr = []
    lenA, lenB = len(A), len(B)
    i = 0
    while True:
        try:
            arr.append(int(A[i]) * int(B[i]))
            i += 1
        except:
            if i >= lenA and i >= lenB:
                break

            if lenA > i:
                arr.append(int(A[i]))
            
            if lenB > i:
                arr.append(int(B[i]))

            i += 1
    
    arr = arr[::-1]
    count = ''
    for i in arr:
        count += str(i)

    if int(count) == num:
        print(1)
    else:
        print(0)
            
