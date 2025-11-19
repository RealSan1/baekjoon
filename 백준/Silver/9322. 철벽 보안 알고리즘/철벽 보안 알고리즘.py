import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    N = int(input())
    num = {}
    key1 = list(map(str, input().split()))
    key2 = list(map(str, input().split()))
    crp = list(map(str, input().split()))

    for i in range(N):
        num[key2[i]] = [crp[i], key1.index(key2[i])]


    res = ''
    for key in sorted(num.items(), key=lambda x: x[1][1]):
        res += key[1][0]
        res += ' '
        
    print(res)