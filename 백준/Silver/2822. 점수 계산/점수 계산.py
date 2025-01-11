info = {}
key = []
value = []
for i in range(8):
    N = int(input())
    info[i+1] = N

A = sorted(info.items(), key=lambda x: x[1], reverse=True)
A = A[:5]

for i, j in A:
    key.append(i)
    value.append(j)
key.sort()

print(sum(value))
print(*key)
