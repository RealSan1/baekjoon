import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    while True:
        temp = arr.copy()
        for i in range(N):
            try:
                arr[i] = abs(temp[i] - temp[i+1])
            except:
                arr[N-1] = abs(temp[0] - temp[-1])

        if all(x == 0 for x in temp):
            print('ZERO')
            break

        if arr in result:
            print('LOOP')
            break
        else:
            result.append(temp)
