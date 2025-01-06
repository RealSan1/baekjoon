import math

dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

N = input()

for i in N:
    if i == '9':
        i = '6'
    
    dic[i] += 1

dic['6'] = math.ceil(dic['6'] / 2)

result = max(dic.values())

print(result)