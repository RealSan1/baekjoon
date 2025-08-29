import sys
input = lambda: sys.stdin.readline().rstrip()

move = [[-1, 2], [-1, -2], [1, 2], [1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]
T = int(input())
for t in range(T):
    N, R1, C1, R2, C2 = map(int, input().split())
    Bool = False
    for i, j in move:
        if R1 + i == R2 and C1 + j == C2:
            Bool = True
            break
    
    if Bool:
        print(f"Case {t+1}: YES")
    else:
        print(f"Case {t+1}: NO")