N, D = map(str, input().split(' '))
var = 0
for i in range(1, int(N)+1):
    var += str(i).count(D)

print(var)