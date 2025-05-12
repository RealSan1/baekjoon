import sys, re
input = sys.stdin.readline

N = int(input())
result = []
for _ in range(N):
    A = input().strip()
    temp = re.sub('[a-z]', ' ', A).split(' ')
    for i in temp:
        if i.isdigit():
            result.append(int(i))
    
for i in sorted(result):
    print(i)