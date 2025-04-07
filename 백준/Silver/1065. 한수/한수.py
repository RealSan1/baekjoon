import sys
input = sys.stdin.readline

N = int(input())
result = 0
for i in range(1, N+1):
    if i < 100:
        result +=1
    else:
        i = str(i)
        div = int(i[1]) - int(i[0])
        Bool = True
        for j in range(len(i)-1):
            if int(i[j]) + div != int(i[j+1]):
                Bool = False
                break
        if Bool:
            result += 1


print(result)