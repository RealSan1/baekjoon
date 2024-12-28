import sys
N = int(input())
for t in range(N):
    arr = [] 

    while len(arr) < 9: 
        line = sys.stdin.readline().strip()
        if line:
            arr.append(list(map(int, line.split())))

    row = []
    col = []
    for i in range(9):
        row.append(arr[i][:])
        col.append([arr[j][i] for j in range(9)])

    valid = True
    for i in range(9):
        if set(row[i]) != set(range(1, 10)) or set(col[i]) != set(range(1, 10)):
            valid = False
            break

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(arr[x + i][y + j])
            if set(subgrid) != set(range(1, 10)):
                valid = False

    if valid:
        print(f"Case {t+1}: CORRECT")
    else:
        print(f"Case {t+1}: INCORRECT")