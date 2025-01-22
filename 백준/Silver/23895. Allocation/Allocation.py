T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    A.sort()    
    for i in A:
        if B - i >= 0:
            B -= i
            result += 1
        else:
            break
    print(f"Case #{t+1}: {result}")