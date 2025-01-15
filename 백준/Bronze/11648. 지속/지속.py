A = list(map(int, input()))
result = 0

while len(A) != 1:
    temp = 1
    for i in range(len(A)):
        temp *= A[i]
    result +=1
    A = list(map(int, str(temp)))

print(result)
    