A, B, C = map(int, input().split()) # A 임대료 B 생산비용 C 노트북 가격

BF = C-B
if BF <= 0 :
    print(-1)
else:
    print(int(A/(C-B)+1))
