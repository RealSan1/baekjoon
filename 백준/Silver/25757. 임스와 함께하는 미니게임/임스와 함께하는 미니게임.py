N, G = map(str, input().split())
arr = []
for i in range(int(N)):
    man = input()
    arr.append(man)

arr = set(arr)

if G == 'Y':
    print(len(arr))

elif G == 'F':
    print(len(arr)//2)

elif G == 'O':
    print(len(arr)//3)