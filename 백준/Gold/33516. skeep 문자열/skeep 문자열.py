import sys
input = sys.stdin.readline

def check_pattern(t):
    target = "skeep"
    for i in range(5):
        c = t[i]
        if i > 0 and c == '0':
            continue
        if c != target[i]:
            return False
    return True

N = int(input())
S = list(input().strip())
count = 0
t = []

for c in S:
    t.append(c)
    while len(t) >= 5:
        window = t[-5:]
        if not check_pattern(window):
            break
        for _ in range(5):
            t.pop()
        t.append('0')
        count += 1

print(count)
