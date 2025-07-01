import sys
input = sys.stdin.readline

N = int(input())
res = 0
userC = {} # 맞춘놈
userW = {} # 틀린놈
for _ in range(N):
    info = list(map(str, input().split()))
    user = info[1] # 유저
    if user == 'megalusion': # 관리자
        continue
    status = int(info[2]) # 상태 4번 정답
    if status == 4:
        userC[user] = 1
    else:
        if user in userC: # 맞춘 사람이 재 제출시
            continue
        else:
            if user in userW:
                userW[user] += 1
            else:
                userW[user] = 1

peC = len(userC) # 문제 맞은 사람 수(분자)
num = peC
for key, value in userW.items():
    if key in userC:
        num += value # 분모

try:
    res = peC / num * 100
    print(res)
except:
    print(0)