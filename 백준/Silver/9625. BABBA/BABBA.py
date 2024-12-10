K = int(input())
A = 0
B = 1
for i in range(1, K):
    var = A + B
    A = B
    B = var
print(A, B)


# A B #
# 0 1 #1
# 1 1 #2
# 1 2 #3
# 2 3 #4
# 3 5 #5