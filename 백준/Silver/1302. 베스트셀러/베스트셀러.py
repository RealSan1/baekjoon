N = int(input())
sell = {}

for i in range(N):
    book = input()
    if book in sell.keys():
        sell[book] += 1
    else:
        sell[book] = 1
        
sort = sorted(sell.items(), key=lambda x: (-x[1], x[0]))
print(sort[0][0])
