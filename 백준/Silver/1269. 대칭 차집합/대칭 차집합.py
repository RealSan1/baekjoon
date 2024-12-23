A, B = map(int ,input().split())
Aset = set(input().split())
Bset = set(input().split())

result = len(Bset - Aset)
result += len(Aset - Bset)
print((result))