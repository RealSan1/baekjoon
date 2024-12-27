A, B = map(int, input().split())

result = int(A - (A * (B * 0.01)))
if result >= 100:
    print(0)
else:
    print(1)