money = int(input())
stock = list(map(int, input().split()))

# 준현
주식 = 0
돈 = money
for i in range(len(stock)):
    if 돈 >= stock[i]:  # 가능한 만큼 매수
        주식 += 돈 // stock[i]
        돈 %= stock[i]
준현 = (stock[-1] * 주식) + 돈  # 최종 자산

# 성민
주식 = 0
돈 = money
상승 = 0
하락 = 0
for i in range(len(stock) - 1):
    if stock[i] < stock[i + 1]:  # 상승
        상승 += 1
        하락 = 0
    elif stock[i] > stock[i + 1]:  # 하락
        하락 += 1
        상승 = 0

    # 매도 조건
    if 상승 == 3 and 주식 != 0:
        돈 += (stock[i + 1] * 주식)
        주식 = 0

    # 매수 조건
    elif 하락 == 3 and 돈 >= stock[i + 1]:
        주식 += 돈 // stock[i + 1]
        돈 %= stock[i + 1]

성민 = (stock[-1] * 주식) + 돈  # 최종 자산

# 결과 비교
if 준현 > 성민:
    print("BNP")
elif 성민 > 준현:
    print("TIMING")
else:
    print("SAMESAME")
