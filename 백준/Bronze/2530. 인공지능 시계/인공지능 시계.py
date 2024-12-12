A, B, C = map(int, input().split())
D = int(input())
H = D // 3600 #시
D %= 3600 #분
M = D // 60
S = D % 60 #초

C += S
B += M
A += H

if C > 59: #초 계산
    B += C // 60
    C = C % 60

if B > 59: #분 계산
    A += B // 60
    B = B % 60

if A > 23: #시 계산
    A = A % 24

print(A, B, C)