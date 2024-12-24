T = int(input())

for _ in range(T):
    A = int(input())
    note_1 = list(map(int, input().split()))

    B = int(input())
    note_2 = list(map(int, input().split()))
    result = set(note_1) & set(note_2)

    for i in range(B):
        if note_2[i] in result:
            print(1)
        else:
            print(0)