A = list(map(int, input()))
B = list(map(int, input()))
A_result = []
B_result = []

while len(A) != len(B):
    if len(A) > len(B):
        B.insert(0,0)
    else:
        A.insert(0,0)

for i in range(len(A)):
    if A[i] > B[i]:
        A_result.append(A[i])
    elif A[i] < B[i]:
        B_result.append(B[i])
    elif A[i] == B[i]:
        A_result.append(A[i])
        B_result.append(B[i])


if len(A_result) == 0:
    A_result = 'YODA'

else:
    A_result = int(''.join(map(str, A_result)))

if len(B_result) == 0:
    B_result = 'YODA'

else:
    B_result = int(''.join(map(str, B_result)))

print(A_result)
print(B_result)