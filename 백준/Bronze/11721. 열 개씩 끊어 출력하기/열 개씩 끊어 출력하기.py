N = input()

if len(N) <= 10:
    print(N)

else:
    for i in range(len(N)//10+1):
        print(N[i*10:(i+1)*10])