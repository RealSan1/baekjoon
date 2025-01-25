A, B = map(str, input().split())
print(int(str(int(A[::-1]) + int(B[::-1]))[::-1]))