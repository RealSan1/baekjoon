T = int(input())
for i in range(T):
    A, B, X = map(int, input().split())
    print(A*(X-1)+B)