import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    W = list(map(str, input().split()))
    num = W.pop(0)

    while W:
        A = W.pop(0)
        if ord(num[0]) < ord(A):
            num += A
        
        elif ord(num[0]) == ord(A):
            A += num
            num = A
            
        elif ord(num[0]) > ord(A):
            A += num
            num = A

    print(num)