N = int(input())
A = ''
for i in range(1, N+1):
    A += str(i)

print(A.index(str(N))+1)