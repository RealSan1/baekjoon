T = int(input())
temp = 0
for _ in range(T):    
    N = int(input()) #학교
    for _ in range(N):
        S, L = map(str, input().split(' ')) #이름 술
        if temp < int(L):
            name = S
        temp = int(L)
    print(name)