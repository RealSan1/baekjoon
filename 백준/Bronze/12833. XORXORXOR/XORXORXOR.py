A, B, C = map(int, input().split())

홀수 = (A ^ B)
짝수 = ((A ^ B) ^ B)
if C % 2 == 0:
    print(짝수)
else:
    print(홀수)
