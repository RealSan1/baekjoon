A, B = map(str, input().split())

A_max = A.replace('5', '6')
B_max = B.replace('5', '6')
max_result = int(A_max) + int(B_max)

A_min = A.replace('6', '5')
B_min = B.replace('6', '5')
min_result = int(A_min) + int(B_min)

print(min_result, max_result)