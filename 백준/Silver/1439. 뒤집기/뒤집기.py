s = input()

result = []
current = s[0]

for char in s[1:]:
    if char == current[-1]: 
        current += char
    else: 
        result.append(current)
        current = char
result.append(current)

A, B = 0, 0
for i in result:
    if i[0] == '0':
        A += 1
    else:
        B += 1

print(min(A,B))