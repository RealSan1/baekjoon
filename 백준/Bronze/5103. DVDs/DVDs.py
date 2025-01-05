while True:
    title = input()
    if title == '#':
        break
    
    M, S = map(int, input().split()) #최대보유, 현재보유
    T = int(input())
    for _ in range(T):
        A, B = map(str, input().split())
        B = int(B)
        if A == 'S':
            S = max(S - B, 0)
        elif A == 'R':
            S = min(S + B, M)

    print(title, S)