import sys

X = int(sys.stdin.readline().rstrip())
arr = []
for i in range(X):
    T = sys.stdin.readline().rstrip().split()
    if T[0] == 'push_front':
        temp = arr
        arr = []
        arr.append(int(T[-1]))
        arr += temp
    
    elif T[0] == 'push_back':
        arr.append(int(T[-1]))

    elif T[0] == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
            arr = arr[1:]
    
    elif T[0] == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())

    elif T[0] == 'size':
        print(len(arr))

    elif T[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif T[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])

    elif T[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
