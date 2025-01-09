T = int(input())
N = input()
result = []
for i in N:
    if i != 'A' and i != 'J' and i != 'V':
        result.append(i)
        
if len(result) == 0:
    print('nojava')
else:
    print("".join(result))