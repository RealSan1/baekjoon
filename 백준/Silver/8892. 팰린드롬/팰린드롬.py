import sys, itertools
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = [0] * K
    result = None
    for V in range(K):
        arr[V] = input().strip()
    
    for i, j in itertools.permutations(arr, 2):
        temp = i+j
        if temp == temp[::-1]:
            result = temp
            break
    
    if result == None:
        print(0)
    else:
        print(result)
