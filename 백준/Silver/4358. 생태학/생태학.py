import sys

info = {}
count = 0

while True:
    Tree = sys.stdin.readline().strip()
    if Tree == '':
        break
    count += 1

    if Tree in info:
        info[Tree] += 1
    else:
        info[Tree] = 1


for key, value in sorted(info.items(), key=lambda x: x[0]):
    print(f"{key} {value/count * 100:.4f}")