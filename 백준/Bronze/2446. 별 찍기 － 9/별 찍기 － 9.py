N = int(input())

for i in range(N, 1, -1):
    star = '*' * ((2*i) -1)
    temp = ' ' * (N-i)
    print(f'{temp}{star}')    
    
for i in range(1, N+1):
    star = '*' * ((2*i) -1)
    temp = ' ' * (N-i)
    print(f'{temp}{star}')