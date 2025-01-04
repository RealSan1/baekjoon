A = input()
if A[0] == '"' and A[-1] == '"' and len(A) > 2:
    print(A[1:-1])
else:
    print('CE')