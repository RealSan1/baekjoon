import sys
from collections import deque
N = int(sys.stdin.readline().strip())
arr = deque()
for _ in range(N):
    A = sys.stdin.readline().strip()

    if A[0] == '1':
        arr.appendleft(int(A[1:]))

    elif A[0] == '2':
        arr.append(int(A[1:]))

    elif A == '3':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())

    elif A == '4':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())

    elif A == '5':
        print(len(arr))

    elif A == '6':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif A == '7':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])

    elif A == '8':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
