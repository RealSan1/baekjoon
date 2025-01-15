import itertools

N = int(input()) # 총 카드 개수
K = int(input()) # 선택카드 개수
arr = []
result = []
for _ in range(N):
    card = input()
    arr.append(card)

result = set("".join(p) for p in itertools.permutations(arr, K))
print(len(result))

