var = 0
for i in range(5):
    A = int(input())
    if A < 40:
        var += 40
    else:
        var += A
print(var//5)