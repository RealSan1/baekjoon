T = int(input())
arr = []
for i in range(T):
    N, M = map(str, input().split(' '))
    N = int(N, base=2)
    M = int(M, base=2)
    print(bin(N+M)[2:])