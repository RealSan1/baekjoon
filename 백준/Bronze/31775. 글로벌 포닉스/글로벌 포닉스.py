import sys
input = sys.stdin.readline

S1 = False
S2 = False
S3 = False
for i in range(3):
    A = input()
    if A[0] == 'l':
        S1 = True
    elif A[0] == 'k':
        S2 = True
    elif A[0] == 'p':
        S3 = True

if S1 and S2 and S3:
    print('GLOBAL')
else:
    print("PONIX")