import sys

X = int(sys.stdin.readline().rstrip())

arr = []
for i in range(X):
    T = sys.stdin.readline().rstrip().split()
    if T[0] == '1':
        arr.append(int(T[-1]))

    elif T[0] == '2':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    
    elif T[0] == '3':
        print(len(arr))

    elif T[0] == '4':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    
    elif T[0] =='5':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])