var = []
A, B, C = map(int, input().split(' '))
if A < B and A < C:
    var.append(A)
    if B < C:
        var.append(B)
        var.append(C)
    else:
        var.append(C)
        var.append(B)
elif B < A and B < C:
    var.append(B)
    if A < C:
        var.append(A)
        var.append(C)
    else:
        var.append(C)
        var.append(A)
elif C < A and C < B:
    var.append(C)
    if A < B:
        var.append(A)
        var.append(B)
    else:
        var.append(B)
        var.append(A)

print(*var)

