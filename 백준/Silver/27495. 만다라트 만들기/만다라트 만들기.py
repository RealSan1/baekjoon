arr = []
for i in range(9):
    A = input().split()
    arr.append(A)

dic = {}

for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        temp = []
        for i in range(3):
            for j in range(3):
                temp.append(arr[x+i][y+j])
        if x != 3 or y != 3: # 최종 목표 제외
            key = temp[4]
            value = temp[:4] + temp[5:] # 원소 4제외
            dic[key] = value

sorted_dict = {k: sorted(v) for k, v in sorted(dic.items(), key=lambda x: x[0])}

i = 0
for key, value in sorted_dict.items():
    i +=1
    j = 0
    print(f"#{i}. {key}")    
    for v in value:
        j +=1
        print(f"#{i}-{j}. {v}")
    