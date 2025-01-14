from itertools import permutations

N = int(input())
boxes = []
for _ in range(N):
    l, w, h = map(int, input().split())
    boxes.append(sorted([l, w, h]))

boxes.sort(key=lambda x: x[0] * x[1] * x[2])

M = int(input())
for _ in range(M):
    item = list(map(int, input().split()))
    item.sort()  
    found = False

    for perm in permutations(item):
        perm = sorted(perm)
        for box in boxes:
            if box[0] >= perm[0] and box[1] >= perm[1] and box[2] >= perm[2]:
                print(box[0] * box[1] * box[2])  
                found = True
                break
        if found:
            break

    if not found:
        print("Item does not fit.")
