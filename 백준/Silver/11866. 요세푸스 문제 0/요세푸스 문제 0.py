# f(n,k)=((f(n−1,k)+k−1)mod n)+1 점화식

N, K =map(int,input().split())
people = list(range(1, N + 1))
var = 0
result = []
for i in range(N):
    var = (var + K - 1) % len(people)
    result.append(people.pop(var))

print('<' + str(result)[1:-1] + '>')