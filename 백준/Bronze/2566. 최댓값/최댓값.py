size = [[0 for i in range(9)]for j in range(9)]
info = []
temp = []
for i in range(9):  # 입력
    row = list(map(int, input().split()))
    for j in range(9):
        size[i][j] = row[j]

for j in range(9):
    for i in range(9):
        temp.append(size[j][i])  # 2차원 -> 1차원 변경
    info.append(max(temp))  # 배열에서 최대값 찾기
    info.append(j+1)  # 배열의 행
    info.append(temp.index(max(temp))+1)  # 최대값 열
    temp = []  # 초기화

temp = info[0]
for i in range(9):
    if temp < info[i*3]:
        temp = info[i*3]
        r = info[i*3+1]
        c = info[i*3+2]
    elif temp == info[i*3]:  # 모든 결과 값이 같은 경우
        temp = info[i * 3]
        r = info[i*3+1]
        c = info[i*3+2]

print(temp)
print(r, c)