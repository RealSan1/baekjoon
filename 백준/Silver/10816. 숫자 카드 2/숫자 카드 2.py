N = int(input())
상근 = list(map(int, input().split()))

M = int(input())
카드 = list(map(int, input().split()))
카드_dict = {i: 0 for i in 카드}

for i in 상근:
    if i in 카드_dict:
        카드_dict[i] += 1
    
print(*[카드_dict[x] for x in 카드])