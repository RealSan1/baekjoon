n = int(input())
for i in range(1, n+1):
    num = sum((map(int, str(i))))
    temp = num + i
    if temp == n:
        print(i)
        break
    
    if i == n:
        print(0)